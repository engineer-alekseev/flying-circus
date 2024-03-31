import aiohttp
import asyncio
import json
import random

AUTH_SERVICE = "http://auth_service:8000"


async def register_user(email, id):
    url = f"{AUTH_SERVICE}/auth_service/auth/register"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "X-Telegram-ID": id,
    }
    data = {"email": email, "telegram_id": id}

    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            response_data = await response.text()
    return response.status


async def info_user(id):
    url = f"{AUTH_SERVICE}/auth_service/auth/user"
    headers = {
        "accept": "application/json",
        "X-Telegram-ID": id,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response_data = await response.text()
            print(response_data)
            return response_data, response.status
        
    


