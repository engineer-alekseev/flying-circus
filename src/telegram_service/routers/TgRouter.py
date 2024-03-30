from fastapi import APIRouter, status,  HTTPException,  Depends
from fastapi.responses import JSONResponse
from routers.schemas import NearestEvents
# import json
# from routers.schemas import RegistrationRequest



class TgRouter():
    def __init__(self):
        self.router = APIRouter(prefix="/tg", tags=["tg"])

        @self.router.post("/send")
        async def send(data:NearestEvents):
           

            return {'code':200, 'data': data.model_dump()}


        