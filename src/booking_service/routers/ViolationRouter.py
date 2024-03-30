from fastapi import APIRouter, status, HTTPException, Depends


from routers.schemas import BookingCreate
from database.Models.Models import Role, User, Room, Booking, Violation
from database.database import get_session, AsyncSession, selectinload, select

from uuid import UUID
from services.utils import get_overlap_bookings, get_user, get_admin
from datetime import timedelta

router = APIRouter(prefix="/violations", tags=["Violations"])


@router.post("/", status_code=201)
async def create_violation(
    admin: User = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    pass


@router.patch("/{id}")
async def set_violation(
    id: UUID,
    admin: User = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    pass
