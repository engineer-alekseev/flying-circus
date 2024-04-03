import subprocess
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

command = "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_service"
output = subprocess.check_output(command, shell=True, text=True)
ALEMBIC_PATH = "/home/alex/my/microservices/src/updater/alembic.ini" #be careful - path should be absolute and it differs on other machine
DB_CONTAINER_IP = output.strip()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_CONTAINER_IP}:{DB_PORT}/{DB_NAME}"

new_sql_url = f"sqlalchemy.url = {DB_URL}"

with open(ALEMBIC_PATH, 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    if line.startswith("sqlalchemy.url = "):
        lines[i] = f"{new_sql_url}\n"
        break

with open(ALEMBIC_PATH, 'w') as file:
    file.writelines(lines)
