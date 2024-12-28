#!/usr/bin/env python3

import asyncio
import logging

import spymarine


async def main():
    logging.basicConfig(
        format="%(levelname)s:%(message)s",
        level=logging.DEBUG,
        filename="debug.log",
        filemode="w",
    )

    print("Start creating a debug report in debug.log")

    async with spymarine.DeviceReader() as reader:
        for _ in range(4):
            await reader.read_sensors()

    print("Finished")


if __name__ == "__main__":
    asyncio.run(main())
