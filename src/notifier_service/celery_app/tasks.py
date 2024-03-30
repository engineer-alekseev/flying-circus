from celery import shared_task
from aiohttp import ClientSession
import asyncio


async def fetch_data():
    data_source_url = (
        "http://booking_service:8000/booking_service/booking/nearest_events"
    )

    # tg_notifier_url = (
    #     "http://telegram_service:8000/.../..."  # TODO(weldonfe): Уточнить у Миши
    # )
    # mail_notifiler_url = "http://mail_service:8000/"
    
    print()
    print()
    print(data_source_url)
    print()
    print()

    try:  # TODO(weldonfe): временный костыль, убрать или перепистать на кастомные исключения
        async with ClientSession() as session:
            async with session.get(data_source_url) as response:
                data = await response.json()
                
                print(data)

            # async with session.post(url=tg_notifier_url, data=data) as response:
            #     tg_response = await response.json()

            # async with session.post(url=mail_notifiler_url, data=data) as response:
            #     mail_response = await response.json()

    except Exception as e:  # TODO(weldonfe): продолжение костыля, см коммент выше
        print(e)


@shared_task
def fetch_data_wrapper():
    asyncio.run(fetch_data())
