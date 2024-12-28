import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, ClassVar, Type

from .property_dict import PropertyDict, PropertyValue


@dataclass
class Sensor(ABC):
    """Represents a sensor of a device"""

    UNIT: ClassVar[str] = ""
    """A string describing the unit of the value property for this sensor"""

    sensor_id: int | None = field(default=None, kw_only=True)
    """A virtual unique identifier of the sensor"""

    value: float = 0.0
    """The current value of the sensor"""

    state_index: int | None = field(
        default=None, repr=False, compare=False, kw_only=True
    )
    """The absolute index in a state PropertyDict"""

    state_offset: int = field(default=0, repr=False, compare=False, kw_only=True)
    """The offset of this sensor's state in a PropertyDict relative to the first
    sensor in a device. Used to define the sensor inside a device."""

    def update(self, property_dict: PropertyDict):
        """Update the sensor value based on a PropertyDict from a state update"""

        assert self.state_index is not None

        try:
            p = property_dict.values[self.state_index]
            self.value = self.convert(p)
        except KeyError:
            logging.error("No sensor value for state index %s", self.state_index)

    @abstractmethod
    def convert(self, p: PropertyValue) -> float:
        """Converts the given PropertyValue to the sensor value in the defined unit"""
        pass

    def asdict(self) -> dict[str, Any]:
        """Convert the sensor to a dict leaving out internal properties. Useful for
        converting a sensor to JSON."""

        assert self.sensor_id is not None
        return {
            "id": self.sensor_id,
            "value": self.value,
            "unit": self.UNIT,
        }


@dataclass
class BarometerSensor(Sensor):
    UNIT: ClassVar[str] = "mbar"

    def convert(self, p: PropertyValue) -> float:
        return p.number


@dataclass
class TemperatureSensor(Sensor):
    UNIT: ClassVar[str] = "celsius"

    def convert(self, p: PropertyValue) -> float:
        return p.second / 10.0


@dataclass
class CurrentSensor(Sensor):
    UNIT: ClassVar[str] = "ampere"

    def convert(self, p: PropertyValue) -> float:
        return p.second / 100.0


@dataclass
class ResistiveSensor(Sensor):
    UNIT: ClassVar[str] = "ohm"

    def convert(self, p: PropertyValue) -> float:
        return p.second


@dataclass
class VoltageSensor(Sensor):
    UNIT: ClassVar[str] = "volt"

    def convert(self, p: PropertyValue) -> float:
        return p.second / 1000.0


@dataclass
class TankVolumeSensor(Sensor):
    UNIT: ClassVar[str] = "liter"

    def convert(self, p: PropertyValue) -> float:
        return p.second / 10.0


@dataclass
class TankLevelSensor(Sensor):
    UNIT: ClassVar[str] = "percentage"

    def convert(self, p: PropertyValue) -> float:
        return p.first / 1000.0


@dataclass
class ChargeSensor(Sensor):
    UNIT: ClassVar[str] = "percentage"

    def convert(self, p: PropertyValue) -> float:
        return p.first / 16000.0


@dataclass
class CapacitySensor(Sensor):
    UNIT: ClassVar[str] = "ampere_hour"

    def convert(self, p: PropertyValue) -> float:
        return p.second / 100.0


def sensor_field(sensory_cls: Type[Sensor], state_offset=0):
    return field(default_factory=lambda: sensory_cls(state_offset=state_offset))
