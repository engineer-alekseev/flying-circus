from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

# Enum for user roles
class UserRoleEnum(enum.Enum):
    admin = 'admin'
    user = 'user'

# SQLAlchemy model for the Users table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(Enum(UserRoleEnum))
    telegram_id = Column(String, unique=True)

# SQLAlchemy model for the Rooms table
class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    capacity = Column(Integer)
    location = Column(String)
    min_time = Column(Integer)
    max_time = Column(Integer)
    photo_link = Column(String)

# SQLAlchemy model for the Bookings table
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    user = relationship("User")
    room = relationship("Room")

# SQLAlchemy model for the Violations table
class Violation(Base):
    __tablename__ = 'violations'

    id = Column(Integer, primary_key=True)
    violation_type = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    user = relationship("User")
    booking = relationship("Booking")


if __name__ == '__main__':
    engine = create_engine('postgresql://username:password@localhost/database')
    Base.metadata.create_all(engine)