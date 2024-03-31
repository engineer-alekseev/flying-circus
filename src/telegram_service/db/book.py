import aiohttp

BOOKING_SERVICE = "http://booking_service:8000"

async def get_data(room,day,id):
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

async def book(room,day,id):
    params = {'booking_date': day}
    headers = {'accept': 'application/json',  "X-Telegram-ID": str(id),}
    url = f'{BOOKING_SERVICE}/booking_service/rooms/{room}/booked_every_15_min'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            data = await response.json()
    return data        
    

