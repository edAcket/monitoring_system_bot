import os
from dotenv import load_dotenv

from src.logger import setup_logger

load_dotenv()
setup_logger()

# Telegram
TG_TOKEN: str = os.getenv("TG_TOKEN", "")
ALLOWED_USERS: list[int] = [
    int(uid.strip()) for uid in os.getenv("ALLOWED_USERS", "").split(",") if uid.strip()
]
PROXY_URL: str = os.getenv("PROXY_URL", "")

# Пороги алертов
TEMP_THRESHOLD: int = int(os.getenv("TEMP_THRESHOLD", 75))
CPU_THRESHOLD: int = int(os.getenv("CPU_THRESHOLD", 85))

# Интервал проверки алертов (секунды)
ALERT_INTERVAL: int = 60


def validate():
    if not TG_TOKEN:
        raise ValueError("TG_TOKEN не задан в .env")
    if not ALLOWED_USERS:
        raise ValueError("ALLOWED_USERS не задан в .env")


validate()
