from typing import Annotated
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class User(BaseModel):
    pass


class RoomInfo(BaseModel):
    pass
    # name: str
    # capacity: int
    # location: str
    # min_time: int
    # max_time: int
    # photo_link: str


class BookingTime(BaseModel):
    pass
    # start_time: datetime
    # end_time: datetime

class BookingInfo(BaseModel):
    pass
#     start_time: datetime
#     end_time: datetime
#     user_id: int
#     room_id: int

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
