from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from enum import Enum


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class AuthMethod(str, Enum):
    NATIVE = "native"
    GOOGLE = "google"
    GITLAB = "gitlab"
    TELEGRAM = "gitlab"


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    telegram_id: str = Field(unique=True)
    email: str = Field(unique=True)
    # email_verified: bool = Field(default=False)

    auth_method: AuthMethod = Field(default=AuthMethod.TELEGRAM)
    role: Role = Field(default=Role.USER)
