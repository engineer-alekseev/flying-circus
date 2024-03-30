import secrets
import jwt
import asyncio
import json
import datetime
import time
from config_reader import config
secret = config.bot_token.get_secret_value()

async def generate_token(id,email):
    t = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=120)
    payload = {"id": id,
               "email":email,
               "exp": t}
    encoded_jwt = jwt.encode(payload = payload,key = secret, algorithm="HS256")
    return encoded_jwt

async def decode_token(jwt_token):
    try:
        decoded_jwt = jwt.decode(jwt = jwt_token,key = secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        decoded_jwt = None
    return decoded_jwt

if __name__ == '__main__':
    a = asyncio.run(generate_token(123))
    b = asyncio.run(decode_token(a))
