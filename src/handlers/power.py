from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.services.proxmox import reboot_host, shutdown_host

power_router = Router()


@power_router.message(Command("shutdown"))
async def cmd_shutdown(message: Message):
    await message.answer("⚠️ Выключаю машину через 10 секунд...")
    ok = shutdown_host()
    if not ok:
        await message.answer("❌ Ошибка выключения")


@power_router.message(Command("reboot"))
async def cmd_reboot(message: Message):
    await message.answer("🔄 Перезагружаю машину...")
    ok = reboot_host()
    if not ok:
        await message.answer("❌ Ошибка перезагрузки")
