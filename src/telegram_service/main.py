import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config_reader import config
from handlers import common, register, info, booking
from fastapi import FastAPI
from routers.TgRouter import TgRouter
import uvicorn

app = FastAPI(
    title="Auth REST Gateway",
    description="Gateway to authentication and authorization",
    version="1.0.0",
    root_path="/telegram_service",
)

app.include_router(TgRouter().router)


async def job():
    # job logic
    pass
    # await bot.send_message(chat_id = 246259983, text= '123')


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.bot_token.get_secret_value())
    routers = (
        common.router,
        register.router,
        info.router,
        booking.router,
    )
    list(map(dp.include_router, routers))
    await dp.start_polling(bot)


async def start_server():
    # Конфигурация и запуск сервера
    config = uvicorn.Config(
        "main:app", host="0.0.0.0", port=8000, loop="asyncio", reload=False
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
