import logging
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.services.host import get_host_stats

status_router = Router()

@status_router.message(Command("status"))
async def cmd_status(message: Message):
    stats = get_host_stats()

    cores = "\n".join(
        f"  Core {i}: <b>{p}%</b>"
        for i, p in enumerate(stats.cpu_per_core)
    )

    await message.answer(
        f"🖥 <b>Статус хоста</b>\n\n"
        f"CPU среднее: <b>{stats.cpu_percent}%</b>\n"
        f"{cores}\n\n"
        f"RAM: <b>{stats.ram_percent}%</b> "
        f"({stats.ram_used_gb:.1f} / {stats.ram_total_gb:.1f} GB)\n"
        f"Uptime: <b>{stats.uptime_hours:.1f}ч</b>",
        parse_mode="HTML"
    )