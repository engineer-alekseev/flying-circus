from fastapi import APIRouter, Depends, HTTPException, status
from services.utils import get_overlap_bookings
from routers.schemas import RoomInfo,  BookingInfo, RoomInfoCreate
from database.database import get_session, select, selectinload
from database.Models.Models import Room, Booking
from datetime import datetime, timedelta

from typing import List
from uuid import UUID

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/", response_model=List[RoomInfo])
async def get_room_list(session=Depends(get_session)):
    q = select(Room)
    rooms = (await session.exec(q)).all()

    return rooms


@router.post("/", status_code=201)
async def create_room(room: RoomInfoCreate, session=Depends(get_session)):
    room = Room(**room.__dict__)
    
    session.add(room)
    await session.commit()
    await session.refresh(room)
    

@router.get("/{id}", response_model=RoomInfo)
async def get_room_list(id: UUID, session=Depends(get_session)):
    q = select(Room).where(Room.id == id)
    room = (await session.exec(q)).first()

    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room with this ID not found",
        )

    return room


@router.get("/{id}/booked", response_model=List[BookingInfo])
async def get_room_list(
    id: UUID,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
    session=Depends(get_session),
):
    
    if not start_time:
        start_time = datetime.now()
    
    if not end_time:
        end_time = start_time.date() + timedelta(days=1)
    
    q = select(Room).where(Room.id == id)
    room = (await session.exec(q)).first()
    
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room with this ID not found",
        )
    
    overlaps = get_overlap_bookings(room.id, start_time, end_time, session)
    
    return overlaps
