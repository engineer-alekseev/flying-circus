from config import TIMEZONE
from fastapi import APIRouter, Depends, HTTPException, status
from services.utils import get_overlap_bookings, get_admin, get_user
from routers.schemas import RoomInfo, BookingInfo, RoomInfoCreate, UserInfo
from database.database import get_session, select, selectinload, AsyncSession, func
from database.Models.Models import Room, Booking, User
from datetime import date, datetime, timedelta

from typing import List
from uuid import UUID

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.get("/", response_model=List[RoomInfo])
async def get_room_list(
    user: UserInfo = Depends(get_user), session: AsyncSession = Depends(get_session)
):
    q = select(Room)
    rooms = (await session.exec(q)).all()

    return rooms


@router.post("/", status_code=201)
async def create_room(
    room: RoomInfoCreate,
    admin: UserInfo = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    q = select(Room).where(Room.name == room.name)
    r = (await session.exec(q)).first()

    if r:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Room with this name already exist",
        )

    room = Room(**room.__dict__)

    session.add(room)
    await session.commit()
    await session.refresh(room)


@router.get("/{id}", response_model=RoomInfo)
async def get_room_list(
    id: UUID,
    user: UserInfo = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
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
    booking_date: date | None = None,
    user: UserInfo = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    if not booking_date:
        booking_date = datetime.now(tz=None).date()

    start_time = datetime.combine(booking_date, datetime.min.time(), tzinfo=None)
    end_time = datetime.combine(
        booking_date + timedelta(days=1), datetime.min.time(), tzinfo=None
    )

    q = select(Room).where(Room.id == id)
    room = (await session.exec(q)).first()

    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room with this ID not found",
        )

    overlaps: List[Booking] = await get_overlap_bookings(
        room.id, start_time, end_time, session
    )

    return overlaps


@router.get("/{id}/booked_every_15_min", response_model=List[int])
async def get_room_list(
    id: UUID,
    booking_date: date | None = None,
    user: UserInfo = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):

    q = select(Room).where(Room.id == id)
    room = (await session.exec(q)).first()

    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room with this ID not found",
        )

    q = select(Booking).where(func.date(Booking.start_time) == booking_date)
    bookings = (await session.exec(q)).all()

    bookings = sorted(bookings, key=lambda x: x.start_time)
    bookings = map(lambda x: x.start_time, bookings)
    bookings = list(bookings)

    booked_96 = [0] * 96

    for i in bookings:
        start_time = i.start_time.time()
        end_time = i.end_time.time()

        hours, minutes = start_time.hour(), start_time.minutes()
        ind_start = hours * 60 + minutes

        hours, minutes = end_time.hour(), end_time.minutes()
        ind_end = hours * 60 + minutes

        for ind in range(ind_start, ind_end):
            booked_96[ind] = 1

    return booked_96
