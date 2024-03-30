import aiohttp
import asyncio
import json
import random

AUTH_SERVICE = "http://auth_service:8000"


async def get_data(day):
    lst = [1 if random.random() > 0.5 else 0 for i in range(96)]
    return lst


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


asyncio.run(register_user("pattycha@student.21-school.ru", f"{246259983}"))
asyncio.run(info_user(f"{246259983}"))
