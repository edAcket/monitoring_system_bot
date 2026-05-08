import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.services.temp import get_temperatures

temp_router = Router()


@temp_router.message(Command("temp"))
async def cmd_temp(message: Message):
    logging.info(f"Запрос /temp от {message.from_user.id}")
    temps = get_temperatures()

    if not temps:
        await message.answer("⚠️ Датчики температуры не найдены")
        return

    lines = "\n".join(f"  {t.sensor_name}: <b>{t.temp:.1f}°C</b>" for t in temps)

    await message.answer(f"🌡 <b>Температуры</b>\n\n{lines}", parse_mode="HTML")
