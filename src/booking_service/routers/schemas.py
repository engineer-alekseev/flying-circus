from typing import Any, List, Optional
from uuid import UUID
from database.Models.Models import AuthMethod, Role
from pydantic import BaseModel, EmailStr, Field, model_validator
from datetime import datetime


class UserInfo(BaseModel):
    id: UUID
    telegram_id: str
    email: EmailStr = Field(pattern=".*@student\.21-school\.ru$")
    auth_method: AuthMethod
    role: Role


class RoomInfoCreate(BaseModel):
    name: str
    location: str
    capacity: int = 4
    min_time: int = 15
    max_time: int = 60
    photo_link: Optional[str]


class RoomInfo(RoomInfoCreate):
    id: UUID


class Interval(BaseModel):
    start_time: datetime
    end_time: datetime

    @model_validator(mode="before")
    def remove_timezone(cls, item: Any) -> Any:
        if isinstance(item, datetime):
            item.replace(tzinfo=None)
        return item


class BookingCreate(Interval):
    room_id: UUID


class BookingInfo(BookingCreate):
    id: UUID
    user_id: UUID


class BookingFullInfo(Interval):
    id: UUID
    user: UserInfo
    room: RoomInfo


class NearestEvents(BaseModel):
    starts_soon: List[BookingFullInfo]
    ends_soon: List[BookingFullInfo]


# class Violation(BaseModel):
#     violation_type: str
#     description: str
#     user_id: int
#     booking_id: int


def to_user_info(item):
    return UserInfo(
        id=item.id,
        telegram_id=item.telegram_id,
        email=item.email,
        auth_method=item.auth_method,
        role=item.role,
    )


def to_room_info(item):
    return RoomInfo(
        id=item.id,
        name=item.name,
        location=item.location,
        capacity=item.capacity,
        min_time=item.min_time,
        max_time=item.max_time,
        photo_link=item.photo_link,
    )


def to_booking_full_info(item):
    return BookingFullInfo(
        id=item.id,
        start_time=item.start_time,
        end_time=item.end_time,
        user=to_user_info(item.user),
        room=to_room_info(item.room),
    )
