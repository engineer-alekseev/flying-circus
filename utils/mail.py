import asyncio
from email.message import EmailMessage
import aiosmtplib

async def send_mail(mail,token):
    message = EmailMessage()
    message["From"] = "not_reply@bytecode.su"
    message["To"] = mail
    message["Subject"] = "Hello World!"
    message.set_content(token)

    await aiosmtplib.send(
        message,
        hostname="smtp.mail.ru",
        port=465,
        use_tls=True,
        username="not_reply@bytecode.su",
        password="rhDM2eyJeHxNRbkjk72C"
    )


asyncio.run(send_mail("ecoms@live.com","123"))