from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from settings import settings

engine = create_async_engine(settings.database_url)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()
