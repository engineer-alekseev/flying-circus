from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Relationship, SQLModel, Field
from enum import Enum
import sqlalchemy as sa

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class AuthMethod(str, Enum):
    NATIVE = "native"
    GOOGLE = "google"
    GITLAB = "gitlab"
    TELEGRAM = "telegram"


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, on_delete="CASCADE")
    telegram_id: str = Field(unique=True)
    email: str = Field(unique=True)
    # email_verified: bool = Field(default=False)

    auth_method: AuthMethod = Field(default=AuthMethod.TELEGRAM)
    role: Role = Field(default=Role.USER)

    bookings: list["Booking"] = Relationship(back_populates="user", on_delete="CASCADE")
    # violations: list["Violation"] = Relationship(back_populates="violations")


class Room(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True)
    location: str
    capacity: int
    min_time: int
    max_time: int
    photo_link: Optional[str]

    bookings: list["Booking"] = Relationship(back_populates="room", cascade="all, delete")


class Booking(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, on_delete="CASCADE")
    start_time: datetime
    end_time: datetime
    user_id: UUID = Field(foreign_key="user.id", on_delete="CASCADE")
    room_id: UUID = Field(foreign_key="room.id", on_delete="CASCADE")

    user: User = Relationship(back_populates="bookings", cascade="all, delete")
    room: Room = Relationship(back_populates="bookings", cascade="all, delete")


class ViolationType(Enum):
    ROOM_NOT_USED = "room_not_used"
    OVERBOOKING = "overbooking"
    INAPPROPRIATE_USAGE = "inappropriate_usage"


class Violation(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    violation_type: ViolationType
    description: str
    user_id: UUID = Field(foreign_key="user.id", on_delete="CASCADE")
    booking_id: UUID = Field(foreign_key="booking.id", on_delete="CASCADE")
    is_active: bool

    # user: list[User] = Relationship(back_populates="user", cascade="all, delete")
    # booking: list[Booking] = Relationship(back_populates="booking", cascade="all, delete")

# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres_service