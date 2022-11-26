from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOSTNAME}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"

if config.BACKEND_DEBUG:
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)
else:
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
