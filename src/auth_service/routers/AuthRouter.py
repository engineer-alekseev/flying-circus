from fastapi import APIRouter, status, HTTPException, Depends

# from services.JWTBearer import JWTBearer
from fastapi.responses import JSONResponse

from routers.schemas import (
    RegistrationRequest,
)
from database.Models.Models import User
from database.database import get_session, AsyncSession, select


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=201)
async def register(
    request: RegistrationRequest, session: AsyncSession = Depends(get_session)
):
    q = select(User).where(User.telegram_id == request.telegram_id)
    user = (await session.exec(q)).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this telegram ID already exist",
        )

    user = User(**request.__dict__)

    session.add(user)
    await session.commit()
    await session.refresh(user)


@router.get("/{telegram_id}", response_model=User)
async def get_user(telegram_id: str, session: AsyncSession = Depends(get_session)):
    q = select(User).where(User.telegram_id == telegram_id)
    user = (await session.exec(q)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this telegram ID not found",
        )

    return user
