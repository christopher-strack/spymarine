# spymarine

A library for spying on Simarine devices and their sensor values using asyncio and Python

Based on the fantastic reverse engineering work of https://github.com/htool/pico2signalk

Only tested with Simarine Pico rev2

## Library Installation

```sh
pip install spymarine
```

## Getting Started

Make sure your Simarine device is configured to use AP or STA Wifi mode. It's not possible
to connect via a local network while in REMOTE mode.

Run the following code on the same network that the Simarine device is connected to:

```python
import asyncio
import spymarine

async def main():
    # Print all devices and their latest sensor values every second
    async with spymarine.DeviceReader() as reader:
        while True:
            await reader.read_sensors()
            print(reader.devices)
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
```

## Troubleshooting

#### Q: `DeviceReader` is stuck while establishing a connection when using STA Wifi mode

- Switch into AP Wifi mode and connect to the Wifi
- Use `reader.write_devices_cache(path)` to create a devices cache
- Construct a `DeviceReader` and using the `devices_cache_path` argument
  while in STA Wifi mode

Note that the cache needs to be regenerated if any hardware of app configuration
change.

## Author

Christopher Strack
