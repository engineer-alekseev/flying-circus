from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
from enum import Enum

# Enum for user roles
class UserRole(str, Enum):
    admin = 'admin'
    user = 'user'

# Pydantic model for the Users table
class User(BaseModel):
    name: str
    email: str
    role: UserRole
    telegram_id: str

# Pydantic model for the Rooms table
class Room(BaseModel):
    name: str
    capacity: int
    location: str
    min_time: int
    max_time: int
    photo_link: str

# Pydantic model for the Bookings table
class Booking(BaseModel):
    start_time: datetime
    end_time: datetime
    user_id: int
    room_id: int

# Pydantic model for the Violations table
class Violation(BaseModel):
    violation_type: str
    description: str
    user_id: int
    booking_id: int

if __name__ == '__main__':
    print(User.schema_json())