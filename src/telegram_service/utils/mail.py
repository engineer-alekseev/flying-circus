import aiohttp
import json

async def send_mail(mail,token):
    url = 'http://mail_service:8000/send_one_message'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'email': mail,
        'message': token
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(data)) as response:
            await response.text()  
            return response.status
    
