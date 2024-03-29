from fastapi import APIRouter, Depends
from routers.schemas import RoomInfo, BookingTime, BookingInfo
from database.database import get_session
from datetime import datetime

from typing import List
from uuid import UUID

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/", response_model=List[RoomInfo])
async def get_room_list(session=Depends(get_session)):

    return [RoomInfo(), RoomInfo()]


@router.get("/{id}", response_model=RoomInfo)
async def get_room_list(id: UUID, session=Depends(get_session)):

    return RoomInfo()


@router.get("/{id}/booked", response_model=List[BookingInfo])
async def get_room_list(
    id: UUID,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
    session=Depends(get_session),
):

    return List[BookingInfo(), BookingInfo()]
