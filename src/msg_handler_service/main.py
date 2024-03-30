from fastapi import FastAPI, APIRouter, HTTPException
from email.message import EmailMessage
import aiosmtplib
import asyncio
from routers.schemas import NearestEvents
import former

app: FastAPI = FastAPI(
    title="mailing",
    description="Service to manage mailing",
    version="0.0.1"
)

router: APIRouter = APIRouter()

@app.post("/", status_code=201)
async def parse_data(request: NearestEvents) -> None:
    data = request.model_dump()

    start_tasks: list = [send_mail(chunk["user"]["email"], former.form_string(former.TimeType.START)) for chunk in data["starts_soon"]]
    end_tasks: list = [send_mail(chunk["user"]["email"], former.form_string(former.TimeType.END)) for chunk in data["ends_soon"]]
    start_tasks.append(*end_tasks)

    await asyncio.gather(*start_tasks)

async def send_mail(mail: str, message: str) -> None:
    email: EmailMessage = EmailMessage()
    email["From"] = "not_reply@bytecode.su"
    email["To"] = mail
    email["Subject"] = "Booking_S21_notify"
    email.set_content(message)

    await aiosmtplib.send(
        email,
        hostname="smtp.mail.ru",
        port=465,
        use_tls=True,
        username="not_reply@bytecode.su",
        password="rhDM2eyJeHxNRbkjk72C"
    )





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8007,
        reload=True,
    )
