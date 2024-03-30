from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from enum import Enum

class Room(BaseModel):
    name: str = Field
    capacity: int = Field
    location: str = Field
    min_time: int = Field
    max_time: int = Field
    photo_link: str = Field