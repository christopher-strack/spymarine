import asyncio
import socket
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import pytest

from spymarine.communication import (
    HEADER_LENGTH,
    Communication,
    Header,
    Message,
    MessageType,
    crc,
    make_request,
    parse_header,
    parse_response,
)
from spymarine.error import ParsingError

from .raw_data import DEVICE_COUNT_RESPONSE, STATE_RESPONSE

TEST_UDP_PORT = 12345
TEST_TCP_PORT = 56789


async def send_udp_broadcast(message: bytes, port: int) -> None:
    BROADCAST_IP = "255.255.255.255"
    addr = (BROADCAST_IP, port)
    loop = asyncio.get_event_loop()
    transport, _ = await loop.create_datagram_endpoint(
        asyncio.DatagramProtocol,
        remote_addr=addr,
        reuse_port=True,
        family=socket.AF_INET,
        proto=socket.IPPROTO_UDP,
        allow_broadcast=True,
    )
    transport.sendto(data=message, addr=addr)
    transport.close()


@asynccontextmanager
async def make_open_communication() -> AsyncGenerator[Communication, None]:
    TIMEOUT = 1  # Timeout after which the communication is cancelled

    communication = Communication(udp_port=TEST_UDP_PORT, tcp_port=TEST_TCP_PORT)

    async with asyncio.timeout(TIMEOUT):
        await communication.create_udp_server()
        await send_udp_broadcast(b"some message", TEST_UDP_PORT)

        try:
            await communication.discover_ip()
            assert communication.ip_address is not None
            await communication.connect()

            yield communication
        finally:
            await communication.close()


@asynccontextmanager
async def open_test_server(handler):
    server = await asyncio.start_server(
        handler,
        "0.0.0.0",
        TEST_TCP_PORT,
    )
    async with server:
        await server.start_serving()

        yield


async def null_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    writer.close()


@pytest.mark.asyncio
async def test_receive_broadcast_message() -> None:
    async with open_test_server(null_handler):
        async with make_open_communication() as communication:
            await send_udp_broadcast(STATE_RESPONSE, TEST_UDP_PORT)
            response = await communication.receive_broadcast()
            assert response == Message(
                type=MessageType.SENSOR_STATE, data=STATE_RESPONSE[HEADER_LENGTH:-2]
            )


@pytest.mark.asyncio
async def test_receive_invalid_broadcast_message() -> None:
    async with open_test_server(null_handler):
        async with make_open_communication() as communication:
            await send_udp_broadcast(b"not a valid message", TEST_UDP_PORT)
            with pytest.raises(ParsingError):
                await communication.receive_broadcast()


async def handle_device_count_client(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
):
    device_count_request = make_request(Message(MessageType.DEVICE_COUNT))

    data = await reader.read(2048)
    assert data == device_count_request

    writer.write(DEVICE_COUNT_RESPONSE)
    await writer.drain()
    writer.close()


@pytest.mark.asyncio
async def test_request_message() -> None:
    async with open_test_server(handle_device_count_client):
        async with make_open_communication() as communication:
            response = await communication.request(Message(MessageType.DEVICE_COUNT))
            assert response.type == MessageType.DEVICE_COUNT


def test_parse_header():
    assert parse_header(
        b"\x00\x00\x00\x00\x00\xff\x41\x85\xde\xc3\x46\x01\x61\xff"
    ) == Header(type=b"\x41", length=353)

    assert parse_header(
        b"\x00\x00\x00\x00\x00\xff\x02\x7f\xfc\xbb\x1f\x00\x11\xff"
    ) == Header(type=b"\x02", length=17)

    assert parse_header(
        b"\x00\x00\x00\x00\x00\xff\xb0\x85\xde\xc3\x46\x01\x14\xff"
    ) == Header(type=b"\xb0", length=276)

    VALID_HEADER = b"\x00\x00\x00\x00\x00\xff\x02\x85\xde\xc3\x46\x00\x11\xff"

    assert parse_header(VALID_HEADER) == Header(type=b"\x02", length=17)

    with pytest.raises(ParsingError):
        # too short
        parse_header(VALID_HEADER[:-1])

    with pytest.raises(ParsingError):
        # pattern mismatch
        parse_header(b"\0x01" + VALID_HEADER[1:])


def test_parse_response():
    VALID_RESPONSE = b"\x00\x00\x00\x00\x00\xff\x02\x85\xde\xc3\x46\x00\x11\xff\x01\x01\x00\x00\x00\x1f\xff\x02\x01\x00\x00\x00\x29\xff\x13\x14"
    assert parse_response(VALID_RESPONSE) == Message(
        type=MessageType.DEVICE_COUNT,
        data=b"\x01\x01\x00\x00\x00\x1f\xff\x02\x01\x00\x00\x00\x29\xff",
    )

    with pytest.raises(ParsingError):
        # invalid length
        response = bytearray(VALID_RESPONSE)
        response[12] = response[12] + 1
        parse_response(bytes(response))

    with pytest.raises(ParsingError):
        # invalid crc
        response = bytearray(VALID_RESPONSE)
        response[-1] = response[-1] + 1
        parse_response(bytes(response))


def test_crc():
    message = b"\x00\x00\x00\x00\x00\xff\x02\x04\x8c\x55\x4b\x00\x03\xff"
    assert crc(message[1:-1]) == 43200
