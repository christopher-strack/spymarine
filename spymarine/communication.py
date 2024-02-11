import asyncio
import copy
import logging
import re
import time
from dataclasses import dataclass
from enum import Enum

from .error import ParsingError


def crc(s: bytes) -> int:
    """Calculate a CRC as accepted by Simarine devices.

    Original source: https://github.com/htool/pico2signalk
    Copyright Erik Bosman / @brainsmoke
    """
    poly = 0x1189
    crc = 0
    for c in s:
        for i in range(8):
            c_msb = (c >> 7) & 1
            crc_msb = (crc >> 15) & 1

            c = (c << 1) & 0xFF
            crc = (crc << 1) & 0xFFFF

            if c_msb ^ crc_msb:
                crc ^= poly
    return crc


class MessageType(Enum):
    """The message type described by the header.
    The enum only represents the known subset.
    """

    DEVICE_COUNT = b"\x02"
    """Request the number of connected devices"""

    DEVICE_INFO = b"\x41"
    """Request information about a device"""

    SENSOR_STATE = b"\xb0"
    """Sensor update message (UDP)"""


@dataclass
class Header:
    """Describes the header of a message"""

    type: bytes
    length: int


HEADER_LENGTH = 14


@dataclass
class Message:
    """A message as received by a Simarine device"""

    type: MessageType
    data: bytes = b""


def parse_header(data: bytes) -> Header:
    """Parses the given bytes. Returns a Header on success.
    Raises ParsingError if the given bytes are not a valid header.
    Note: The header is not fully understood and might not work on
    all Simarine devices.
    """

    if match := re.match(
        b"\x00\x00\x00\x00\x00\xff(.)\x85\xde\xc3\x46(..)\xff", data[:HEADER_LENGTH]
    ):
        return Header(type=match[1], length=int.from_bytes(match[2]))
    else:
        raise ParsingError(f"Invalid header {data[:HEADER_LENGTH]!r}")


def parse_response(raw_response: bytes) -> Message:
    """Parse a response from a Simarine device. Returns a Message on success.
    Raises ParsingError if the given data is not a valid or known Simarine Message.
    """

    header = parse_header(raw_response[:HEADER_LENGTH])
    data_length = len(raw_response[HEADER_LENGTH - 1 :])

    if header.length != data_length:
        raise ParsingError(
            f"Incomplete response ({data_length} of {header.length} bytes received)",
        )

    calculated_crc = crc(raw_response[1:-3]).to_bytes(2)
    received_crc = raw_response[-2:]
    if calculated_crc != received_crc:
        raise ParsingError(f"Invalid crc ({received_crc!r} != {calculated_crc!r})")

    try:
        return Message(
            type=MessageType(header.type), data=raw_response[HEADER_LENGTH:-2]
        )
    except ValueError:
        raise ParsingError(f"Unknown message type {header.type.hex()}")


def make_request(message: Message) -> bytes:
    """Returns a valid Simarine request for the given Message."""

    length = 3 + len(message.data)
    header = b"\x00\x00\x00\x00\x00\xff%b\x04\x8c\x55\x4b%b\xff"
    data = header % (message.type.value, length.to_bytes(2)) + message.data
    return data + crc(data[1:-1]).to_bytes(2)


def make_device_request(device_id: int) -> Message:
    """Returns a device request for the given Device ID. The Simarine device
    will reply with a device response that contains the description of the
    device."""

    data = b"\x00\x01\x00\x00\x00%b\xff\x01\x03\x00\x00\x00\x00\xff\x00\x00\x00\x00\xff"
    return Message(
        type=MessageType.DEVICE_INFO,
        data=data % device_id.to_bytes(1),
    )


# UDP port used by Simarine devices to announce sensor changes
UDP_PORT = 43210

# TCP port used by Simarine devices to exchange request/response messages
TCP_PORT = 5001


Address = tuple[str, int]


class UdpMessage:
    """Represents a UDP message. Used to share state between objects."""

    def __init__(self, data: bytes, addr: Address) -> None:
        self.data = data
        self.addr = addr


class UDPServerProtocol(asyncio.DatagramProtocol):
    """Implements a UDP protocol that notifies the given event when a new UDP message
    is received and writes it to the given message."""

    def __init__(self, event: asyncio.Event, message: UdpMessage) -> None:
        self.event = event
        self.message = message

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.transport = transport

    def datagram_received(self, data: bytes, addr: Address) -> None:
        self.message.data = data
        self.message.addr = addr
        logging.debug("UDP broadcast message received")
        self.event.set()


class Communication:
    """Communicate with Simarine devices by making requests and listening
    for broadcast messages.

    Simarine devices communicate via TCP and UDP broadcast messages.
    UDP broadcast messages report new sensor values in short intervals and
    can be used to discover the device. TCP is used to request specific
    information and probably make changes to the device."""

    def __init__(self, udp_port=UDP_PORT, tcp_port=TCP_PORT) -> None:
        self.udp_port = udp_port
        self.tcp_port = tcp_port
        self.ip_address: str | None = None

        self._udp_event = asyncio.Event()
        self._latest_udp_message = UdpMessage(b"", ("", 0))
        self._udp_transport: asyncio.transports.DatagramTransport | None = None
        self._last_request_time: float | None = None

    async def open(self) -> None:
        """Discovers a Simarine device and opens a connection over UDP"""

        if self._udp_transport is None:
            await self.init()  # pragma: no cover

        if self.ip_address is None:
            logging.info("Connecting to Simarine device...")

            udp_message = await self._receive_udp()
            self.ip_address, _ = udp_message.addr

            logging.info("Found device at %s:%s", self.ip_address, self.tcp_port)

    def close(self) -> None:
        """Closes an open connection"""

        if self._udp_transport is not None:
            logging.info("Disconnecting from Simarine device...")
            logging.debug("Stop UDP server")
            self._udp_transport.close()
            self._udp_transport = None
            self.ip_address = None

    async def __aenter__(self):
        await self.open()  # pragma: no cover

    async def __aexit__(self, exc_t, exc_v, exc_tb):
        self.close()  # pragma: no cover

    async def request(self, message: Message, request_limit: float = 0.1) -> Message:
        """Send a request to a Simarine device over TCP and returns a response
        Raises ParsingError in case no valid response has been returned.
        Limits time between requests as defined by request_limit"""

        assert self.ip_address is not None

        try:
            await self._wait_for_request_delay(request_limit)

            logging.debug("Connecting to %s:%i...", self.ip_address, self.tcp_port)
            reader, writer = await asyncio.open_connection(
                self.ip_address, self.tcp_port
            )

            logging.debug("Requesting %r", message.type.name)
            writer.write(make_request(message))
            await writer.drain()

            data = await reader.read(1024)
            response = parse_response(data)

            logging.debug("Closing connection")
            writer.close()
            await writer.wait_closed()

        finally:
            self._last_request_time = time.time()

        return response

    async def receive_broadcast(self) -> Message:
        """Receive the next incoming UDP message
        Raises ParsingError in case the next message is invalid."""

        assert self._udp_transport is not None
        udp_message = await self._receive_udp()
        response = parse_response(udp_message.data)
        logging.debug("Received broadcast message %r", response.type.name)
        return response

    async def init(self):
        """Initializes the communication by starting the UDP server.
        Automatically done by open()"""

        if self._udp_transport is None:
            self._udp_transport = await self._create_udp_server()

    async def _wait_for_request_delay(self, request_limit: float):
        if self._last_request_time is not None:
            seconds_since_last_request = time.time() - self._last_request_time
            if seconds_since_last_request < request_limit:
                await asyncio.sleep(request_limit - seconds_since_last_request)

    async def _create_udp_server(self):
        """Create an UDP broadcast server that listens to incoming messages"""

        logging.debug("Start UDP broadcast server on port %s", self.udp_port)
        loop = asyncio.get_event_loop()
        transport, _ = await loop.create_datagram_endpoint(
            lambda: UDPServerProtocol(self._udp_event, self._latest_udp_message),
            local_addr=("0.0.0.0", self.udp_port),
            reuse_port=True,
        )
        return transport

    async def _receive_udp(self) -> UdpMessage:
        """Waits until the next UDP broadcast message is received and returns it"""

        logging.debug("Waiting for UDP broadcast message")
        await self._udp_event.wait()
        message = copy.copy(self._latest_udp_message)
        self._udp_event.clear()
        return message
