from datetime import datetime, timedelta
from typing import List
from uuid import UUID
from routers.schemas import BookingCreate, UserInfo
from database.database import get_session, AsyncSession, select, and_, or_, func
from database.Models.Models import Booking, Role, Room, User, Violation
from fastapi import Depends, Request, HTTPException, status
import httpx
from config import AUTH_SERVICE
import requests


def get_user(request: Request) -> UserInfo:
    url = f"http://{AUTH_SERVICE}/auth/user"

    # ! DEBUG DELETE
    headers = dict(request.headers)
    # headers["X-Telegram-ID"] = "123456782"
    # ! DEBUG DELETE

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text,
        )

    user = response.json()
    print("RESPONSE:", user)
    user = UserInfo(**user)

    return user


async def get_admin(user: UserInfo = Depends(get_user)) -> UserInfo:
    if user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No administrator rights",
        )

    return user


async def get_overlap_bookings(
    room_id: UUID,
    start_time: datetime,
    end_time: datetime,
    session: AsyncSession = Depends(get_session),
) -> List[Booking]:
    # start_time = start_time.replace(tzinfo=None)
    # end_time = end_time.replace(tzinfo=None)

    overlap_cond = or_(
        and_(Booking.start_time <= start_time, start_time < Booking.end_time),
        and_(Booking.start_time < end_time, end_time <= Booking.end_time),
        and_(start_time <= Booking.start_time, Booking.end_time <= end_time),
    )

    q = select(Booking).where(Booking.room_id == room_id).where(overlap_cond)
    overlaps = (await session.exec(q)).all()

    return overlaps


async def check_booking(
    booking: BookingCreate,
    room: Room,
    user: UserInfo = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):

    if booking.start_time <= datetime.now(tz=None):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can not book room in the past",
        )

    min_time = timedelta(minutes=room.min_time)
    max_time = timedelta(minutes=room.max_time)
    delta = booking.end_time - booking.start_time

    if not min_time <= delta <= max_time:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect booking time. Min time: {} Max time: {} Requested time: {}".format(
                room.min_time, room.max_time, delta
            ),
        )

    q = select(Violation).where(
        Violation.user_id == user.id and Violation.is_active == True
    )
    violations = (await session.exec(q)).first()

    if violations:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user is limited to book rooms due violation restriction",
        )

    q = select(Booking).where(
        Booking.user_id == user.id
        and func.date(Booking.start_time) == booking.start_time.date()
    )
    peer_booking = (await session.exec(q)).first()

    if peer_booking:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"This peer already booked room on this date: {booking.start_time.date()}",
        )
