"""Базовый DAO класс"""

from datetime import datetime 
from typing import Generic, TypeVar
from sqlalchemy import select, insert, update, delete

from database import async_session_maker

T = TypeVar("T")


class BaseDAO(Generic[T]):
    """Базовый DAO класс"""

    model: T = None

    @classmethod
    async def find_by_id(cls, model_id: int | str) -> T | None:
        """Поиск одной или никакой записи по id"""
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter: dict) -> T | None:
        """Поиск одной или никакой записи по фильтру"""
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all_with_filter(cls, **filter: dict) -> list[T]:
        """Поиск всех записей по фильтру"""
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data: dict) -> T:
        """Добавление новой записи"""
        cleaned_data = remove_timezones(data)
        async with async_session_maker() as session:
            query = insert(cls.model).values(**cleaned_data).returning(cls.model)
            data = await session.execute(query)
            await session.commit()
            return data.scalars().one()

    @classmethod
    async def update(cls, model_id: int | str, **data: dict) -> T:
        """Обновление записи по id"""
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .where(cls.model.id == model_id)
                .values(**data)
                .returning(cls.model)
            )
            data = await session.execute(query)
            await session.commit()
            return data.scalars().one()

    @classmethod
    async def delete(cls, model_id: int | str) -> None:
        """Удаление записи по id"""
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()

def remove_timezones(data: dict):
    """Очищает все datetime значения в данных от информации о временной зоне."""
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.replace(tzinfo=None)
    return data
