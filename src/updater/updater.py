import subprocess
import os

command = "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_service"
output = subprocess.check_output(command, shell=True, text=True)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_CONTAINER_IP = output.strip()
DB_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_CONTAINER_IP}:{DB_PORT}/{DB_NAME}"


print(DB_CONTAINER_IP)
print(DB_URL)