from datetime import datetime
from uuid import UUID
from database.database import get_session, AsyncSession, select
from database.Models.Models import Booking, Role, Room, User
from fastapi import Depends, Request, HTTPException, status
import httpx
from config import AUTH_SERVICE


async def get_user(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{AUTH_SERVICE}/auth/user", headers=request.headers
        )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        user = User(**response.json())

        return user


async def get_admin(user: User = Depends(get_user)):
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
):
    overlap_cond = (
        (Booking.start <= start_time < Booking.end)
        or (Booking.start < end_time <= Booking.end)
        or (start_time <= Booking.start and Booking.end <= end_time)
    )

    q = select(Booking).where(Booking.room_id == room_id).where(overlap_cond)
    overlaps = (await session.exec(q)).all()

    return overlaps
