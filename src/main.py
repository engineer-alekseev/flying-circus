from fastapi import FastAPI

from settings import settings
from booking.router import router as booking_router

app = FastAPI(
    title="School 21 booking API"
)

app.include_router(booking_router)
