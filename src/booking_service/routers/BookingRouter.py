from fastapi import APIRouter, status, HTTPException, Depends


from routers.schemas import BookingCreate
from database.Models.Models import Role, User, Room, Booking, Violation
from database.database import get_session, AsyncSession, selectinload, select

from uuid import UUID
from services.utils import get_overlap_bookings, get_user
from datetime import timedelta

router = APIRouter(prefix="/booking", tags=["Booking"])


@router.post("/", status_code=201)
async def create_booking(
    booking: BookingCreate,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    q = select(Violation).where(
        Violation.user_id == user.id and Violation.is_active == True
    )
    violations = (await session.exec(q)).first()

    if violations:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user is limited in booking rooms",
        )

    q = select(Room).where(Room.id == booking.room_id)
    room = (await session.exec(q)).first()

    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room with this ID not found",
        )

    min_time = timedelta(minutes=room.min_time)
    max_time = timedelta(minutes=room.max_time)
    delta = booking.end_time.minute - booking.start_time

    if not min_time <= delta <= max_time:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect booking time. Min time: {} Max time: {} Requested time: {}".format(
                room.min_time, room.max_time, delta
            ),
        )

    overlaps = get_overlap_bookings(
        room.id, booking.start_time, booking.end_time, session
    )

    if overlaps != []:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Room is already booked in this time",
        )

    booking = Booking(**booking.__dict__, user=user)

    session.add(booking)
    await session.commit()
    await session.refresh(booking)


@router.delete("/{id}", status_code=204)
async def delete_booking(
    id: UUID,
    user: User = Depends(get_user),
    session: AsyncSession = Depends(get_session),
):
    q = select(Booking).where(Booking.id == id)
    booking = (await session.exec(q)).first()

    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking with this ID not found",
        )

    if booking.user_id != user.id and user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to delete this booking",
        )

    await session.delete(booking)
    await session.commit()
