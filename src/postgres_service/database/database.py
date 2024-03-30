from database.Models.User import User
from database.Models.Booking import Booking
from database.Models.Rooms import Room
from database.Models.Violation import Violation

from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy_utils import database_exists, create_database
from config import DB_URL

print("DB_URL:", DB_URL)

engine = create_engine(DB_URL, echo=True)

def init_db():
    global engine
    if not database_exists(engine.url):
        create_database(engine.url)
    print("Initialize database models")
    SQLModel.metadata.create_all(engine)
    print("Finish Initializing database models")


def get_session():
    with Session(engine) as session:
        yield session