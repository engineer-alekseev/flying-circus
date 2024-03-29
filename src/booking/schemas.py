from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr
from datetime import datetime

class RoomPost(BaseModel):
    name: str
    floor: int
    capacity: int

class RoomDB(RoomPost):
    id: int

class RoomOut(RoomDB):
    pass

