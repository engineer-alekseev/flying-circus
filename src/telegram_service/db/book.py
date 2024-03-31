import aiohttp

BOOKING_SERVICE = "http://booking_service:8000"

async def del_booking(b_id,id):
    url = f'{BOOKING_SERVICE}/booking_service/booking/{str(b_id)}'
    headers = {'accept': 'application/json',"X-Telegram-ID": str(id)}
    async with aiohttp.ClientSession() as session:
        async with session.delete(url, headers=headers) as response:
            await response.json()  # предполагается, что ответ в формате JSON
            return response.status

async def get_bookings_by_user(id):
    url = f'{BOOKING_SERVICE}/booking_service/booking/by_user'
    headers = {'accept': 'application/json',"X-Telegram-ID": str(id)}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response_data = await response.json()  # предполагается, что ответ в формате JSON
            return response_data

async def get_books(room,day,id):
    params = {'booking_date': day}
    headers = {'accept': 'application/json',
                       "X-Telegram-ID": str(id),}
    url = f'{BOOKING_SERVICE}/booking_service/rooms/{room}/booked_every_15_min'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            data = await response.json()
    return data
async def fetch_rooms(id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{BOOKING_SERVICE}/booking_service/rooms/', headers={'accept': 'application/json',  "X-Telegram-ID": str(id)}) as response:
            return await response.json()

async def book(start,end,room,id):
    payload = {
            "start_time": start,
            "end_time": end,
            "room_id": room
            }
    headers = {'accept': 'application/json',  "X-Telegram-ID": str(id),}
    url = f'{BOOKING_SERVICE}/booking_service/booking'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            data = await response.json()
    return data        
    

