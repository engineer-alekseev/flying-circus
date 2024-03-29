from dotenv import load_dotenv
import os

load_dotenv()

AUTH_GRPC_CHANNEL=os.getenv("AUTH_GRPC_CHANNEL")
