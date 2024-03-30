from celery import shared_task
from aiohttp import ClientSession
import asyncio


@shared_task
def print_hello():
    print("Hello World")


# @shared_task(name='fetch_data')
# async def fetch_data():
#     url = "http://httpbin.org/get"
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.text()
#             print(data)


async def fetch_data():
    url = "http://booking_service:8000/booking_service/booking/nearest_events"
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Response from {url}: {data[:100]}...")

@shared_task
def fetch_data_wrapper():
    asyncio.run(fetch_data())




