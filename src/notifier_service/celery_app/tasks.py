from celery import shared_task
from aiohttp import ClientSession
import asyncio


async def fetch_data():
    data_source_url = (
        "http://booking_service:8000/booking_service/booking/nearest_events"
    )

    tg_notifier_url = (
        "http://telegram_service:8000/tg/send"  # TODO(weldonfe): Уточнить у Миши
    )

    mail_notifier_url = "http://mail_service:8000/"

    try:
        async with ClientSession() as session:
            async with session.get(data_source_url) as response:
                data = await response.json()

            async with session.post(url=tg_notifier_url, json=data) as response:
                tg_response = await response.json()

            async with session.post(url=mail_notifier_url, json=data) as response:
                mail_response = await response.json()

    except Exception as e:
        print(e)


@shared_task
def fetch_data_wrapper():
    asyncio.run(fetch_data())
