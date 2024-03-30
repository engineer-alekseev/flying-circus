import aiohttp

BOOKING_SERVICE = "http://booking_service:8000"

async def get_data(day):
    rooms = await fetch_rooms()
    params = {'booking_date': day}
    headers = {'accept': 'application/json'}
    for room in rooms:
        url = f'http://localhost:8001/booking_service/rooms/{room['id']}/booked_every_15_min'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                room['data'] = await response.json()  
    return rooms

async def fetch_rooms():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8001/booking_service/rooms/', headers={'accept': 'application/json'}) as response:
            rooms = await response.json()
            return rooms


        
    

