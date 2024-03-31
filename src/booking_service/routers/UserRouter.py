from typing import List
from fastapi import APIRouter, Depends
from routers.schemas import UserInfo
from database.Models.Models import User
from database.database import get_session, AsyncSession, select
from services.utils import get_admin

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", status_code=200, response_model=List[UserInfo])
async def create_violation(
    admin: UserInfo = Depends(get_admin),
    session: AsyncSession = Depends(get_session),
):
    q = select(User)
    users = (await session.exec(q)).all()
    return users
