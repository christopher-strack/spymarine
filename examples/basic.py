#!/usr/bin/env python3

import asyncio
import logging

import spymarine


async def main():
    logging.basicConfig(level=logging.INFO)

    # Print all devices and their latest sensor values every second
    async with spymarine.DeviceReader() as reader:
        while True:
            await reader.read_sensors()
            print(reader.devices)
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
