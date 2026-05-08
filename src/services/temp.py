import psutil
import subprocess
from dataclasses import dataclass


@dataclass
class TempStats:
    sensor_name: str
    temp: float


SENSOR_NAMES = {
    "k10temp": "CPU",
    "nvme": "SSD",
    "amdgpu": "GPU",
    "acpitz": "ACPI",
    "r8169_0_100:00": "LAN",
    "spd5118": "RAM",
    "mt7921_phy0": "WiFi",
}

def get_temperatures() -> list[TempStats]:
    temps = []
    try:
        sensors = psutil.sensors_temperatures()
        for sensor_name, entries in sensors.items():
            if sensor_name not in SENSOR_NAMES:
                continue
            display_name = SENSOR_NAMES[sensor_name]
            for entry in entries:
                if entry.current > 0:
                    label = entry.label or "core"
                    temps.append(TempStats(
                        sensor_name=f"{display_name} ({label})",
                        temp=entry.current,
                    ))
    except AttributeError:
        temps = _get_temps_from_cli()

    return temps

def _get_temps_from_cli() -> list[TempStats]:
    result = subprocess.run(["sensors", "-u"], capture_output=True, text=True)
    temps = []
    current_sensor = "unknown"

    for line in result.stdout.splitlines():
        line = line.strip()
        if line and not line.startswith(" ") and line.endswith(":"):
            current_sensor = line[:-1]
        elif "temp" in line and "input:" in line:
            try:
                value = float(line.split("input:")[1].strip())
                temps.append(TempStats(sensor_name=current_sensor, temp=value))
            except (ValueError, IndexError):
                continue

    return temps


def get_max_temp() -> float | None:
    temps = get_temperatures()
    if not temps:
        return None
    return max(t.temp for t in temps)
