from fastapi import APIRouter, status, HTTPException, Depends


from routers.schemas import BookingTime
from database.Models.User import User
from database.database import get_session
from sqlmodel import Session, select
from uuid import UUID
from services.utils import get_user


router = APIRouter(prefix="/booking", tags=["Booking"])


@router.post("/", status_code=201)
async def get_room_list(
    booking_time: BookingTime,
    user: User = Depends(get_user),
    session=Depends(get_session),
):
    return


@router.delete("/{id}", status_code=204)
async def get_room_list(
    id: UUID,
    user: User = Depends(get_user),
    session=Depends(get_session),
):
    return
