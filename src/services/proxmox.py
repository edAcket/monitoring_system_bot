import subprocess
import json
import logging


def get_vms() -> list[dict]:
    try:
        result = subprocess.run(
            ["pvesh", "get", "/nodes/localhost/qemu", "--output-format", "json"],
            capture_output=True,
            text=True,
            timeout=5
        )
        vms = json.loads(result.stdout)
        return vms
    except Exception as e:
        logging.error(f"Ошибка получения VM: {e}")
        return []


def vm_action(vmid: int, action: str) -> bool:
    """action: start | stop | reboot"""
    try:
        subprocess.run(
            ["qm", action, str(vmid)],
            capture_output=True,
            text=True,
            timeout=10
        )
        return True
    except Exception as e:
        logging.error(f"Ошибка {action} VM {vmid}: {e}")
        return False