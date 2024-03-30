from datetime import datetime
from typing import List
from uuid import UUID
from routers.schemas import UserInfo
from database.database import get_session, AsyncSession, select, and_, or_
from database.Models.Models import Booking, Role, Room, User
from fastapi import Depends, Request, HTTPException, status
import httpx
from config import AUTH_SERVICE
import requests


def get_user(request: Request) -> UserInfo:
    url = f"http://{AUTH_SERVICE}/auth/user"

    # ! DEBUG DELETE
    headers = dict(request.headers)
    headers["X-Telegram-ID"] = "123456789"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.detail,
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
    start_time = start_time.replace(tzinfo=None)
    end_time = end_time.replace(tzinfo=None)

    overlap_cond = or_(
        and_(Booking.start_time <= start_time, start_time < Booking.end_time),
        and_(Booking.start_time < end_time, end_time <= Booking.end_time),
        and_(start_time <= Booking.start_time, Booking.end_time <= end_time),
    )

    q = select(Booking).where(Booking.room_id == room_id).where(overlap_cond)
    overlaps = (await session.exec(q)).all()

    return overlaps
