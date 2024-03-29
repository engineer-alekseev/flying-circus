from routers.schemas import User
from database.database import get_session, Session
from fastapi import Depends


async def get_user(session: Session = Depends(get_session)):

    return User()
