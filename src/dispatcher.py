import logging

from aiogram import Bot, Dispatcher
from src.handlers import main_router
# from src.handlers.status import status_router
# from src.handlers.temp import temp_router
# from src.handlers.vm import vm_router

from aiogram.client.session.aiohttp import AiohttpSession

from src.config import PROXY_URL, TG_TOKEN, ALLOWED_USERS

async def auth_middleware(handler, event, data):
    user = getattr(event, "from_user", None)
    if user is None or user.id not in ALLOWED_USERS:
        logging.warning(f"Доступ запрещён для user_id={getattr(user, 'id', '?')}")
        if hasattr(event, "answer"):
            await event.answer("⛔ Доступ запрещён")
        return
    return await handler(event, data)


async def main():
    session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else None
    bot = Bot(token=TG_TOKEN, session=session)
    dp = Dispatcher()

    dp.message.middleware(auth_middleware)
    dp.include_router(main_router)

    # await bot.send_message(ALLOWED_USERS[0], "🟢 Бот запущен!")
    # dp.include_router(status_router)
    # dp.include_router(temp_router)
    # dp.include_router(vm_router)

    logging.info("Бот запущен")
    await dp.start_polling(bot)