from typing import List
from fastapi import APIRouter, status, HTTPException, Depends


from routers.schemas import BookingCreate, UserInfo, ViolationCreate, ViolationInfo
from database.Models.Models import Role, User, Room, Booking, Violation
from database.database import get_session, AsyncSession, selectinload, select

from uuid import UUID
from services.utils import get_overlap_bookings, get_user, get_admin
from datetime import timedelta

router = APIRouter(prefix="/violations", tags=["Violations"])


@router.post("/", status_code=201)
async def create_violation(
    violation: ViolationCreate,
    admin: UserInfo = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    q = select(Violation).where(Violation.booking_id == violation.booking_id)
    v = (await session.exec(q)).first()

    if v:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User, attached to this booking, was already punished",
        )

    q = select(User).where(User.id == violation.user_id)
    user = (await session.exec(q)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this ID not found",
        )

    if user.role == Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin can not punish an other admin",
        )

    violation = Violation(**violation.model_dump())
    session.add(violation)
    await session.commit()
    await session.refresh(violation)


@router.patch("/{id}")
async def set_violation(
    id: UUID,
    violation: ViolationCreate,
    admin: UserInfo = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    q = select(Violation).where(Violation.id == id)
    v = (await session.exec(q)).first()
    if not v:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Violation with this id does not exsist",
        )

    violation = Violation(id=id, **violation.model_dump())
    session.add(violation)
    await session.commit()
    await session.refresh(violation)


@router.delete("/{id}")
async def delete_violation(
    id: UUID,
    admin: UserInfo = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    q = select(Violation).where(Violation.id == id)
    violation = (await session.exec(q)).first()

    if not violation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Violation with this id does not exsist",
        )

    await session.delete(violation)
    await session.commit()


@router.get("/", status_code=200, response_model=List[ViolationInfo])
async def create_violation(
    admin: UserInfo = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    q = select(Violation)
    violations = (await session.exec(q)).all()
    return violations
