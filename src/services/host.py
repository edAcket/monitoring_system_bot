import psutil
import time
from dataclasses import dataclass


@dataclass
class HostStats:
    cpu_percent: float
    cpu_per_core: list[float]
    ram_total_gb: float
    ram_used_gb: float
    ram_percent: float
    uptime_hours: float


def get_host_stats() -> HostStats:
    mem = psutil.virtual_memory()
    uptime = (time.time() - psutil.boot_time()) / 3600

    return HostStats(
        cpu_percent=psutil.cpu_percent(interval=1),
        cpu_per_core=psutil.cpu_percent(interval=1, percpu=True),
        ram_total_gb=mem.total / (1024 ** 3),
        ram_used_gb=mem.used / (1024 ** 3),
        ram_percent=mem.percent,
        uptime_hours=uptime,
    )