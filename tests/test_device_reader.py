import json
from unittest.mock import AsyncMock

import pytest

from spymarine.communication import Communication, parse_response
from spymarine.device_reader import DeviceReader

from . import data, raw_data


def make_mock_communication(tcp_responses=[], udp_responses=[]) -> AsyncMock:
    communication = AsyncMock(spec=Communication)
    communication.open = AsyncMock()
    communication.close = AsyncMock()
    communication.request = AsyncMock(side_effect=map(parse_response, tcp_responses))
    communication.receive_broadcast = AsyncMock(
        side_effect=map(parse_response, udp_responses)
    )
    return communication


@pytest.mark.asyncio
async def test_open_requests_devices() -> None:
    communication = make_mock_communication(
        tcp_responses=[raw_data.DEVICE_COUNT_RESPONSE] + raw_data.DEVICE_INFO_RESPONSES
    )
    async with DeviceReader(communication=communication) as reader:
        assert reader.devices == data.DEVICES


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "sensor_response,sensor_data",
    [
        (raw_data.STATE_RESPONSE, data.SENSOR_DATA),
        (raw_data.STATE_RESPONSE2, data.SENSOR_DATA2),
    ],
)
async def test_read_sensors_updates_sensor_values(sensor_response, sensor_data) -> None:
    communication = make_mock_communication(
        tcp_responses=[raw_data.DEVICE_COUNT_RESPONSE] + raw_data.DEVICE_INFO_RESPONSES,
        udp_responses=[sensor_response],
    )

    async with DeviceReader(communication=communication) as reader:
        await reader.read_sensors()
        assert reader.sensors == sensor_data


@pytest.mark.asyncio
async def test_read_sensor_ignores_invalid_messages() -> None:
    communication = make_mock_communication(
        tcp_responses=[raw_data.DEVICE_COUNT_RESPONSE] + raw_data.DEVICE_INFO_RESPONSES,
        udp_responses=[raw_data.UNKNOWN_RESPONSE],
    )

    async with DeviceReader(communication=communication) as reader:
        await reader.read_sensors()
        assert reader.devices == data.DEVICES


@pytest.mark.asyncio
async def test_jsonify_devices():
    communication = make_mock_communication(
        tcp_responses=[raw_data.DEVICE_COUNT_RESPONSE] + raw_data.DEVICE_INFO_RESPONSES
    )
    async with DeviceReader(communication=communication) as reader:
        devices_json_str = json.dumps([device.asdict() for device in reader.devices])
        assert json.loads(devices_json_str) == data.DEVICES_JSON
