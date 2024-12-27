from spymarine import (
    Barometer,
    BarometerSensor,
    Battery,
    BatteryType,
    CapacitySensor,
    ChargeSensor,
    CurrentDevice,
    CurrentSensor,
    FluidType,
    PicoInternal,
    ResistiveDevice,
    ResistiveSensor,
    Tank,
    TankLevelSensor,
    TankVolumeSensor,
    TemperatureDevice,
    TemperatureSensor,
    VoltageDevice,
    VoltageSensor,
)

DEVICES = [
    Barometer(
        device_id=5,
        name="Barometer",
        pressure=BarometerSensor(sensor_id=300, value=0.0),
    ),
    PicoInternal(
        device_id=6,
        name="PICO INTERNAL",
        voltage=VoltageSensor(sensor_id=500, value=0.0),
    ),
    CurrentDevice(
        device_id=10, name="ORION XS", current=CurrentSensor(sensor_id=1100, value=0.0)
    ),
    CurrentDevice(
        device_id=11, name="MPPT", current=CurrentSensor(sensor_id=1300, value=0.0)
    ),
    CurrentDevice(
        device_id=12, name="OTHERS", current=CurrentSensor(sensor_id=1500, value=0.0)
    ),
    CurrentDevice(
        device_id=13,
        name="ANDERSON SOCKETS",
        current=CurrentSensor(sensor_id=1700, value=0.0),
    ),
    CurrentDevice(
        device_id=15,
        name="SC303 [2396]",
        current=CurrentSensor(sensor_id=2000, value=0.0),
    ),
    VoltageDevice(
        device_id=16,
        name="SC303 [2396] 1",
        voltage=VoltageSensor(sensor_id=2200, value=0.0),
    ),
    VoltageDevice(
        device_id=17,
        name="SC303 [2396] 2",
        voltage=VoltageSensor(sensor_id=2300, value=0.0),
    ),
    ResistiveDevice(
        device_id=18,
        name="SC303 [2396] 1",
        resistance=ResistiveSensor(sensor_id=2400, value=0.0),
    ),
    ResistiveDevice(
        device_id=19,
        name="SC303 [2396] 2",
        resistance=ResistiveSensor(sensor_id=2500, value=0.0),
    ),
    ResistiveDevice(
        device_id=20,
        name="SC303 [2396] 3",
        resistance=ResistiveSensor(sensor_id=2600, value=0.0),
    ),
    Battery(
        device_id=21,
        name="HOTEL",
        capacity=200.0,
        battery_type=BatteryType.LIFEPO4,
        charge=ChargeSensor(sensor_id=2700, value=0.0),
        remaining_capacity=CapacitySensor(sensor_id=2701, value=0.0),
        current=CurrentSensor(sensor_id=2702, value=0.0),
        voltage=VoltageSensor(sensor_id=2703, value=0.0),
    ),
    Battery(
        device_id=22,
        name="CAR",
        capacity=70.0,
        battery_type=BatteryType.WET_LOW_MAINTENANCE,
        charge=ChargeSensor(sensor_id=3200, value=0.0),
        remaining_capacity=CapacitySensor(sensor_id=3201, value=0.0),
        current=CurrentSensor(sensor_id=3202, value=0.0),
        voltage=VoltageSensor(sensor_id=3203, value=0.0),
    ),
    Tank(
        device_id=23,
        name="CLEAN WATER",
        capacity=108.0,
        fluid_type=FluidType.FRESH_WATER,
        volume=TankVolumeSensor(sensor_id=3700, value=0.0),
        level=TankLevelSensor(sensor_id=3701, value=0.0),
    ),
    TemperatureDevice(
        device_id=24,
        name="INSIDE",
        temperature=TemperatureSensor(sensor_id=3800, value=0.0),
    ),
    TemperatureDevice(
        device_id=25,
        name="OUTSIDE",
        temperature=TemperatureSensor(sensor_id=3900, value=0.0),
    ),
    VoltageDevice(
        device_id=28,
        name="ST107 [4495] 1",
        voltage=VoltageSensor(sensor_id=4200, value=0.0),
    ),
    VoltageDevice(
        device_id=29,
        name="ST107 [4495] 2",
        voltage=VoltageSensor(sensor_id=4300, value=0.0),
    ),
    VoltageDevice(
        device_id=30,
        name="ST107 [4495] 3",
        voltage=VoltageSensor(sensor_id=4400, value=0.0),
    ),
    ResistiveDevice(
        device_id=31,
        name="ST107 [4495] 1",
        resistance=ResistiveSensor(sensor_id=4500, value=0.0),
    ),
    ResistiveDevice(
        device_id=32,
        name="ST107 [4495] 2",
        resistance=ResistiveSensor(sensor_id=4600, value=0.0),
    ),
    ResistiveDevice(
        device_id=33,
        name="ST107 [4495] 3",
        resistance=ResistiveSensor(sensor_id=4700, value=0.0),
    ),
    ResistiveDevice(
        device_id=34,
        name="ST107 [4495] 4",
        resistance=ResistiveSensor(sensor_id=4800, value=0.0),
    ),
    Tank(
        device_id=36,
        name="GAS",
        capacity=20.0,
        fluid_type=FluidType.FUEL,
        volume=TankVolumeSensor(sensor_id=5000, value=0.0),
        level=TankLevelSensor(sensor_id=5001, value=0.0),
    ),
    Tank(
        device_id=38,
        name="WASTE WATER ",
        capacity=86.0,
        fluid_type=FluidType.WASTE_WATER,
        volume=TankVolumeSensor(sensor_id=5100, value=0.0),
        level=TankLevelSensor(sensor_id=5101, value=0.0),
    ),
]
