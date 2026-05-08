from aiogram import Router
from src.handlers.start import start_router
from src.handlers.status import status_router
from src.handlers.temp import temp_router
from src.handlers.vm import router_vm


main_router = Router()
main_router.include_router(start_router)
main_router.include_router(status_router)
main_router.include_router(temp_router)
main_router.include_router(router_vm)
