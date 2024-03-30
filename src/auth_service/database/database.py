import os
from database.Models.Models import User, Role
from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URL

engine = create_async_engine(DB_URL, echo=True, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as session:
        await session.run_sync(SQLModel.metadata.create_all)

    async with async_session() as session:  # This creates an AsyncSession object
        admin = User(
            email="pintoved@student.21-school.ru",
            telegram_id="123456789",
            role=Role.ADMIN,
        )
        q = select(User).where(User.email == admin.email)
        user = (await session.execute(q)).first()  # Use `execute` instead of `exec`
        if not user:
            session.add(admin)
            await session.commit()
            await session.refresh(admin)


async def get_session():
    async with async_session() as session:
        yield session