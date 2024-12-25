import logging
from typing import AsyncIterator

from .communication import (
    Communication,
    Message,
    MessageType,
    make_device_request,
)
from .device import Device, NullDevice, UnknownDevice, device_from_property_dict
from .error import ParsingError
from .property_dict import PropertyDict, parse_property_dict
from .sensor import Sensor


class DeviceReader:
    """
    Read the current state for devices in a Simarine setup.
    It has only been tested with the Simarine Pico rev2.

    Note that only one device can be connected at the same time including the Simarine app.

    open() will connect and read all device information. Afterwards devices are accessible
    via the devices property.

    read_sensors() will wait for a state update message and update the sensor values of all
    devices.
    """

    def __init__(self, communication: Communication | None = None) -> None:
        """Creates a new device reader"""

        self.communication = Communication() if communication is None else communication
        self.devices: list[Device] = []
        self.sensors: list[Sensor] = []

    async def open(self) -> None:
        """Opens the communication with a Simarine device and requests all device
        information or loads them from a file.
        """

        await self.communication.create_udp_server()
        await self.communication.discover_ip()
        await self.communication.connect()
        self._set_devices(list([device async for device in self._request_devices()]))

    async def close(self):
        """Closes an open communication"""

        await self.communication.close()

    async def read_sensors(self) -> None:
        """Waits for a broadcast message and updates all sensor values"""

        try:
            response = await self.communication.receive_broadcast()
            while response.type != MessageType.SENSOR_STATE:
                response = await self.communication.receive_broadcast()
            property_dict = parse_property_dict(response.data)

            for device in self.devices:
                device.update_sensors(property_dict)
        except ParsingError as e:
            logging.debug(e)

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, exc_t, exc_v, exc_tb):
        await self.close()

    async def _request_device_count(self) -> int:
        return _parse_device_count_response(
            await self.communication.request(Message(type=MessageType.DEVICE_COUNT))
        )

    async def _request_devices(self) -> AsyncIterator[Device]:
        logging.info("Fetching device infos")
        sensor_start_index = 0
        for device_id in range(await self._request_device_count()):
            device_response = await self.communication.request(
                make_device_request(device_id)
            )
            property_dict = _parse_device_response(device_response)
            device = device_from_property_dict(device_id, property_dict)
            device.initialize_sensor_indices(sensor_start_index)
            if not isinstance(device, (NullDevice, UnknownDevice)):
                yield device
            sensor_start_index += device.SENSOR_INDEX_OFFSET

    def _set_devices(self, devices):
        self.devices = devices
        self.sensors = [
            sensor
            for device in self.devices
            for _, sensor in device.sensors
            if sensor.sensor_id is not None
        ]


def _parse_device_count_response(response: Message) -> int:
    if response.type == MessageType.DEVICE_COUNT and len(response.data) >= 6:
        return response.data[5] + 1
    else:
        raise ParsingError(f"Couldn't get device count. Unexpected response {response}")


def _parse_device_response(response: Message) -> PropertyDict:
    if response.type == MessageType.DEVICE_INFO:
        return parse_property_dict(response.data)
    else:
        raise ParsingError(f"Couldn't get device info. Unexpected response {response}")
