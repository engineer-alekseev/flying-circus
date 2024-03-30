from fastapi import APIRouter, status,  HTTPException,  Depends
from fastapi.responses import JSONResponse
from routers.schemas import NearestEvents
# import json
# from routers.schemas import RegistrationRequest



class TgRouter():
    def __init__(self,bot):
        self.router = APIRouter(prefix="/tg", tags=["tg"])
        self.bot = bot
        @self.router.post("/send")
        async def send(data:NearestEvents):
            print(data.model_dump())
            for i in data.model_dump()["starts_soon"]:
                await bot.send_message(chat_id = int(i['user']['telegram_id']),text = "Ваша бронь переговорки скоро начнется")
            for i in data.model_dump()["ends_soon"]:
                await bot.send_message(chat_id = int(i['user']['telegram_id']),text = "Ваша бронь переговорки скоро закончится")
            return {'code':200, 'data': data.model_dump()}


        