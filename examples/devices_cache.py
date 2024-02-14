#!/usr/bin/env python3

import argparse
import asyncio
import logging
import pathlib

from spymarine.device_reader import DeviceReader


async def main(devices_cache_path: pathlib.Path) -> None:
    logging.basicConfig(level=logging.DEBUG)

    # If the script is stuck connecting, try using the Simarine's AP
    # Wifi mode to create the cache. Afterwards DeviceReader will no longer
    # establish a connection but simply listen to UDP broadcast messages.
    cache_exists = devices_cache_path.exists()
    async with DeviceReader(
        devices_cache_path=devices_cache_path if cache_exists else None
    ) as reader:
        if not cache_exists:
            logging.info("Creating devices cache")
            devices_cache_path.parent.mkdir(parents=True, exist_ok=True)
            reader.write_devices_cache(devices_cache_path)

        while True:
            await reader.read_sensors()
            print(reader.devices)
            await asyncio.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Spymarine Devices Cache Example",
        description="Prints sensor data every second. Creates a devices cache if it "
        "doesn't exist. Uses the cached data if available.",
    )
    parser.add_argument(
        "--cache-path",
        type=pathlib.Path,
        default=pathlib.Path.home() / ".spymarine/devices.pickle",
    )
    args = parser.parse_args()

    asyncio.run(main(args.cache_path))
