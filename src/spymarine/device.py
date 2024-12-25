import logging
from dataclasses import dataclass, fields
from enum import Enum
from typing import Any, ClassVar, Iterable

from .property_dict import PropertyDict
from .sensor import (
    BarometerSensor,
    CapacitySensor,
    ChargeSensor,
    CurrentSensor,
    ResistiveSensor,
    Sensor,
    TankLevelSensor,
    TankVolumeSensor,
    TemperatureSensor,
    VoltageSensor,
    sensor_field,
)


class FluidType(Enum):
    FRESH_WATER = 1
    FUEL = 2
    WASTE_WATER = 3


class BatteryType(Enum):
    WET_LOW_MAINTENANCE = 1
    WET_MAINTENANCE_FREE = 2
    AGM = 3
    DEEP_CYCLE = 4
    GEL = 5
    LIFEPO4 = 6


@dataclass
class Device:
    """Represents a device in a Simarine setup.

    A device has a name, static properties describing the device and one or more sensors
    that are regularly updated."""

    TYPE: ClassVar[str] = ""
    """String describing the type of device"""

    SENSOR_INDEX_OFFSET: ClassVar[int] = 0
    """The size of the device inside a state update. Defines how many
    values have to be skipped to get to the next device."""

    device_id: int
    """A unique identifier of the device as provided by the Simarine device"""

    name: str
    """The name of the device as configured by the user"""

    @property
    def sensors(self) -> Iterable[tuple[str, Sensor]]:
        """Iterator for all sensors and their property name of this device"""

        for f in fields(self):
            attr = getattr(self, f.name)
            if isinstance(attr, Sensor):
                yield f.name, attr

    def update_sensors(self, property_dict: PropertyDict) -> None:
        """Update all sensors for this device. Should be called when a state update
        has been received."""

        for _, sensor in self.sensors:
            sensor.update(property_dict)

    def asdict(self) -> dict[str, Any]:
        """Convert the device to a dict leaving out internal properties. Useful for
        converting a device to JSON."""

        def convert_value(obj):
            if isinstance(obj, Enum):
                return obj.name.lower()
            if isinstance(obj, Sensor):
                return obj.asdict()
            return obj

        d: dict = {f.name: convert_value(getattr(self, f.name)) for f in fields(self)}

        d["type"] = self.TYPE

        return d

    def initialize_sensor_indices(self, state_start_index: int) -> None:
        """Needs to be called after a device has been constructed to initialize
        all its sensors. This is cecessary for processing state updates."""

        for index, (_, sensor) in enumerate(self.sensors):
            sensor.state_index = state_start_index + sensor.state_offset
            # We have "virtual" sensors that might have the same state_index so let's
            # assign a unique index to each sensor. To avoid ids overlapping with the next
            # device we scale the available range
            sensor.sensor_id = state_start_index * 100 + index


@dataclass
class PicoInternal(Device):
    TYPE: ClassVar[str] = "pico_internal"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 6

    voltage: VoltageSensor = sensor_field(VoltageSensor)


@dataclass
class Battery(Device):
    TYPE: ClassVar[str] = "battery"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 5

    capacity: float
    battery_type: BatteryType

    charge: ChargeSensor = sensor_field(ChargeSensor, 0)
    remaining_capacity: CapacitySensor = sensor_field(CapacitySensor, 0)
    current: CurrentSensor = sensor_field(CurrentSensor, 1)
    voltage: VoltageSensor = sensor_field(VoltageSensor, 2)


@dataclass
class Tank(Device):
    TYPE: ClassVar[str] = "tank"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 1

    capacity: float
    fluid_type: FluidType

    volume: TankVolumeSensor = sensor_field(TankVolumeSensor, 0)
    level: TankLevelSensor = sensor_field(TankLevelSensor, 0)


@dataclass
class TemperatureDevice(Device):
    TYPE: ClassVar[str] = "temperature"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 1

    temperature: TemperatureSensor = sensor_field(TemperatureSensor)


@dataclass
class Barometer(Device):
    TYPE: ClassVar[str] = "barometer"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 2

    pressure: Sensor = sensor_field(BarometerSensor)


@dataclass
class VoltageDevice(Device):
    TYPE: ClassVar[str] = "voltage"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 1

    voltage: VoltageSensor = sensor_field(VoltageSensor)


@dataclass
class CurrentDevice(Device):
    TYPE: ClassVar[str] = "current"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 2

    current: CurrentSensor = sensor_field(CurrentSensor)


@dataclass
class ResistiveDevice(Device):
    TYPE: ClassVar[str] = "resistive"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 1

    resistance: Sensor = sensor_field(ResistiveSensor)


@dataclass
class NullDevice(Device):
    TYPE: ClassVar[str] = "null"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 0


@dataclass
class UnknownDevice(Device):
    TYPE: ClassVar[str] = "unknown"
    SENSOR_INDEX_OFFSET: ClassVar[int] = 1


def device_from_property_dict(device_id: int, property_dict: PropertyDict) -> Device:
    """Converts a PropertyDict describing a device into the corresponding Device object"""

    device_type = property_dict.values[1][1]

    if device_type == 0:
        return NullDevice(device_id=device_id, name="<null>")
    elif device_type == 1:
        if property_dict.strings[3] == "PICO INTERNAL":
            return PicoInternal(device_id=device_id, name=property_dict.strings[3])
        else:
            return VoltageDevice(device_id=device_id, name=property_dict.strings[3])
    elif device_type == 2:
        return CurrentDevice(device_id=device_id, name=property_dict.strings[3])
    elif device_type == 3:
        return TemperatureDevice(device_id=device_id, name=property_dict.strings[3])
    elif device_type == 4:
        return UnknownDevice(device_id=device_id, name="<unknown>")
    elif device_type == 5:
        return Barometer(device_id=device_id, name=property_dict.strings[3])
    elif device_type == 6:
        return ResistiveDevice(device_id=device_id, name=property_dict.strings[3])
    elif device_type == 7:
        return UnknownDevice(device_id=device_id, name="<unknown>")
    elif device_type == 8:
        return Tank(
            device_id=device_id,
            name=property_dict.strings[3],
            capacity=property_dict.values[7][1] / 10.0,
            fluid_type=FluidType(property_dict.values[6][1]),
        )
    elif device_type == 9:
        return Battery(
            device_id=device_id,
            name=property_dict.strings[3],
            capacity=property_dict.values[5][1] / 100.0,
            battery_type=BatteryType(property_dict.values[8][1]),
        )
    elif device_type == 10:
        return UnknownDevice(device_id=device_id, name="<unknown>")
    elif device_type == 14:
        return UnknownDevice(device_id=device_id, name="<unknown>")

    logging.error("Invalid device type %d", device_type)
    return UnknownDevice(device_id=device_id, name="<unknown>")
