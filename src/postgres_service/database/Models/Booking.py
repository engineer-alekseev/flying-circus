from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from enum import Enum

class Booking(SQLModel, table=True):
    start_time: Field
    end_time: Field
    user_id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, unique=True)
    room_id: Optional[UUID] = Field(unique=True)