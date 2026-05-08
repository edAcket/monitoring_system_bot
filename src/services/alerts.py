import asyncio
import logging
from src.services.temp import get_temperatures
from src.config import TEMP_THRESHOLD, ALLOWED_USERS, ALERT_INTERVAL


async def monitor_temps(bot):
    logging.info("Мониторинг температуры запущен")
    while True:
        try:
            temps = get_temperatures()
            for t in temps:
                if t.temp >= TEMP_THRESHOLD:
                    logging.warning(f"Перегрев: {t.sensor_name} = {t.temp}°C")
                    await bot.send_message(
                        ALLOWED_USERS[0],
                        f"🔥 <b>Перегрев!</b>\n\n"
                        f"{t.sensor_name}: <b>{t.temp:.1f}°C</b>\n"
                        f"Порог: {TEMP_THRESHOLD}°C",
                        parse_mode="HTML",
                    )
        except Exception as e:
            logging.error(f"Ошибка мониторинга температуры: {e}")

        await asyncio.sleep(ALERT_INTERVAL)
