from dataclasses import dataclass, field

from .error import ParsingError

PropertyId = int


@dataclass
class PropertyValue:
    """Value in a PropertyDict that can either represent two independent 2 byte numbers
    or a single 4 byte number"""

    data: bytes
    """Raw bytes representing the value"""

    @property
    def first(self) -> int:
        """Returns the 2 first bytes as a number"""
        return self[0]

    @property
    def second(self) -> int:
        """Returns the 2 last bytes as a number"""
        return self[1]

    @property
    def number(self) -> int:
        """Returns all 4 bytes as a number"""
        return int.from_bytes(self.data)

    def __getitem__(self, index) -> int:
        start = index * 2
        end = start + 2
        return int.from_bytes(self.data[start:end], signed=True)


@dataclass
class PropertyDict:
    """Intermediate representation of certain Simarine responses"""

    strings: dict[PropertyId, str] = field(default_factory=lambda: {})
    values: dict[PropertyId, PropertyValue] = field(default_factory=lambda: {})


def parse_property_dict(data: bytes) -> PropertyDict:
    """Converts bytes received by a Simarine devices to a PropertyDict.
    Raises ParsingError in case the given bytes do not contain a valid
    PropertyDict."""

    property_dict = PropertyDict()

    while data:
        bytes_read = _parse_property(data, property_dict)
        data = data[bytes_read:]

    return property_dict


def _parse_property(data: bytes, d: PropertyDict) -> int:
    if len(data) < 2:
        raise ParsingError("Couldn't parse property")

    property_id = data[0]
    property_type = data[1]
    if property_type == 1:
        d.values[property_id] = PropertyValue(data=data[2:6])
        return 7
    elif property_type == 3:
        d.values[property_id] = PropertyValue(data=data[7:11])
        return 12
    elif property_type == 4:
        data = data[7:]
        pos = data.find(b"\x00")
        data = data[:pos]

        # It looks like a custom encoding is used for strings. Special
        # characters will unfortunately not works as expected.
        d.strings[property_id] = data.decode("ascii", errors="replace")

        return 7 + pos + 2
    raise ParsingError(f"Unknown property type {property_type}")
