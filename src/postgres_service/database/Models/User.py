from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from enum import Enum

# Enum for user roles
class UserRole(str, Enum):
    admin = 'admin'
    user = 'user'

# Pydantic model for the Users table
class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    telegram_id: str = Field(unique=True)
    name: str = Field(unique=True)
    email: str = Field(unique=True)
    role: UserRole
    telegram_id: str