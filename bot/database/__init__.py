"""Подключение к PostgreSQL и управление сессиями"""
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from bot.config import settings

# движок для асинхронной работы с PostgreSQL
engine = create_async_engine(settings.db_url, echo=False)

# фабрика сессий
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """Получить сессию БД для работы"""
    async with async_session() as session:
        yield session
