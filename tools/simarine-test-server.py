#!/usr/bin/env python3

import asyncio
import logging

from data import (
    DEVICE_COUNT_RESPONSE,
    DEVICE_INFO_RESPONSES,
    STATE_RESPONSE,
)

from spymarine.communication import (
    DEFAULT_TCP_PORT,
    DEFAULT_UDP_PORT,
    MessageType,
    parse_response,
)


class SimarineTestServer:
    def __init__(
        self,
        udp_port=DEFAULT_UDP_PORT,
        tcp_port=DEFAULT_TCP_PORT,
        broadcast_interval=1.0,
    ):
        self.udp_port = udp_port
        self.tcp_port = tcp_port
        self.broadcast_interval = broadcast_interval

    async def run(self):
        await asyncio.gather(
            self._run_broadcast_state_server(),
            self._run_tcp_server(),
        )

    async def _run_broadcast_state_server(self):
        logging.info("Start UDP broadcast server")

        broadcast_ip = "255.255.255.255"

        transport, _ = await asyncio.get_running_loop().create_datagram_endpoint(
            lambda: asyncio.DatagramProtocol(),
            local_addr=("0.0.0.0", 0),
            allow_broadcast=True,
        )

        while True:
            transport.sendto(STATE_RESPONSE, (broadcast_ip, self.udp_port))
            await asyncio.sleep(self.broadcast_interval)

    async def _run_tcp_server(self):
        logging.info("Start TCP server")

        server = await asyncio.start_server(
            lambda r, w: self._handle_client(r, w), "0.0.0.0", self.tcp_port
        )

        async with server:
            await server.serve_forever()

    async def _handle_client(self, reader, writer):
        while not writer.is_closing():
            data = await reader.read(2048)
            if data:
                addr = writer.get_extra_info("peername")
                if response := await self._handle_request(data, addr):
                    writer.write(response)
                    await writer.drain()
            else:
                writer.close()

        await writer.wait_closed()

    async def _handle_request(self, data, addr):
        logging.info("Received %d bytes from %s", len(data), addr)

        if message := parse_response(data):
            # the real device is stricter and doesn't allow for making
            # arbitrary requests in any order, but this is good enough
            # for now
            if message.type == MessageType.DEVICE_COUNT:
                logging.info("Reply with device count")
                return DEVICE_COUNT_RESPONSE
            elif message.type == MessageType.DEVICE_INFO:
                device_id = message.data[5]
                logging.info("Reply with device info %d", device_id)
                return DEVICE_INFO_RESPONSES[device_id]
        else:
            logging.info("Invalid request %r", data)


async def main():
    logging.basicConfig(level=logging.INFO)

    server = SimarineTestServer()
    await server.run()


asyncio.run(main())
