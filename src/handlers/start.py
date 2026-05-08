from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "🟢 Proxmox бот активен!\n\n"
        "Доступные команды:\n"
        "/status — статус хоста\n"
        "/temp — температуры\n"
        "/vms — список VM\n"
        "/start_vm <id> — запустить VM\n"
        "/stop_vm <id> — остановить VM\n"
        "/shutdown — выключить машину\n"
        "/reboot — перезагрузить машину\n"
    )
