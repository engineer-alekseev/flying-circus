import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_reader import config
from handlers import common, register, info, booking, my_bookings
from fastapi import FastAPI
from routers.TgRouter import TgRouter
import uvicorn

# Спаривание ежа со слоном, часть первая
# скрещиваем фастапи с тг ботом


dp = Dispatcher(storage=MemoryStorage())
bot = Bot(config.bot_token.get_secret_value())

app = FastAPI(
    title="Auth REST Gateway",
    description="Gateway to authentication and authorization",
    version="1.0.0",
    root_path="/telegram_service",
)

app.include_router(TgRouter(bot).router)

async def main():

    routers = (
        common.router,
        register.router,
        info.router,
        booking.router,
        my_bookings.router
    )
    list(map(dp.include_router, routers))
    await dp.start_polling(bot)


async def start_server():
    # Конфигурация и запуск сервера
    config = uvicorn.Config(
        "main:app", host="0.0.0.0", port=8000, loop="asyncio", reload=True
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()  # Создание нового событийного цикла
    asyncio.set_event_loop(loop)  # Установка событийного цикла в качестве текущего

    task_web = loop.create_task(start_server())
    task_bot = loop.create_task(main())
    gathered_tasks = asyncio.gather(task_web, task_bot)
    loop.run_until_complete(gathered_tasks)
