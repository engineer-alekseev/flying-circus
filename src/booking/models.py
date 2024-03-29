import datetime
from decimal import Decimal
from typing import Optional
from sqlalchemy import UUID, String, func, ForeignKey, Numeric, Integer

from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(255))
    floor: Mapped[int] = mapped_column(Integer)
    capacity: Mapped[int] = mapped_column(Integer)