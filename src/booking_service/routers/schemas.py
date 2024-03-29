from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime, timedelta

class RoomInfoCreate(BaseModel):
    name: str
    location: str
    capacity: int
    min_time: int
    max_time: int
    photo_link: Optional[str]

class RoomInfo(RoomInfoCreate):
    id: UUID

class BookingCreate(BaseModel):
    start_time: datetime
    end_time: datetime
    room_id: UUID

class BookingInfo(BookingCreate):
    id: UUID
    user_id: UUID

# class Booking(BaseModel):
#     start_time: datetime
#     end_time: datetime
#     user_id: int
#     room_id: int


# class Violation(BaseModel):
#     violation_type: str
#     description: str
#     user_id: int
#     booking_id: int
