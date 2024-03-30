from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from enum import Enum

class Violation(SQLModel, table=True):
    violation_type: str = Field(default="None")
    description: str = Field(default="None")
    user_id: Optional[UUID] = Field(default_factory=uuid4)
    booking_id: Optional[UUID] = Field(default_factory=uuid4)