from fastapi import APIRouter, status, HTTPException, Depends

# from services.JWTBearer import JWTBearer
from fastapi.responses import JSONResponse

from routers.schemas import (
    RegistrationRequest,
)
from database.Models.User import User
from database.database import get_session
from sqlmodel import Session, select


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=201)
async def register(
    request: RegistrationRequest, session: Session = Depends(get_session)
):

    user = session.exec(
        select(User).where(User.telegram_id == request.telegram_id)
    ).first()

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this telegram ID already exist",
        )

    user = User(**request.__dict__)

    session.add(user)
    session.commit()
    session.refresh(user)


@router.get("/{telegram_id}", response_model=User)
async def get_user(telegram_id: str, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.telegram_id == telegram_id)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with this telegram ID not found",
        )

    return user
