from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST") 
DB_PORT = os.getenv("DB_PORT_POSTGRES")
DB_USER = os.getenv("DB_USER_2")
DB_NAME = os.getenv("DB_NAME_POSTGRES")
DB_PASSWORD = os.getenv("DB_PASSWORD_POSTGRES")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

#TO ASK VITYA!
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES"))
