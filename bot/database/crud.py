"""CRUD операции с базой данных"""
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import Channel, Download, User


async def get_or_create_user(
    session: AsyncSession,
    telegram_id: int,
    username: str | None,
    full_name: str,
) -> User:
    """Получить юзера или создать нового"""
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    user = result.scalar_one_or_none()

    if user is None:
        user = User(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user


async def get_active_channels(session: AsyncSession) -> list[Channel]:
    """Получить все каналы для обязательной подписки"""
    result = await session.execute(select(Channel))
    return list(result.scalars().all())


async def get_cached_download(
    session: AsyncSession, instagram_url: str
) -> Download | None:
    """Получить кэш по ссылке, если не протух"""
    result = await session.execute(
        select(Download).where(
            Download.instagram_url == instagram_url,
            Download.expires_at > datetime.now(),
        )
    )
    download = result.scalar_one_or_none()

    # обновляем счетчик если кэш найден
    if download:
        download.download_count += 1
        await session.commit()

    return download


async def save_download(
    session: AsyncSession,
    instagram_url: str,
    file_id: str,
    media_type: str,
) -> Download:
    """Сохранить скачанный файл в кэш"""
    # может уже быть запись с протухшим кэшем — обновим её
    result = await session.execute(
        select(Download).where(Download.instagram_url == instagram_url)
    )
    download = result.scalar_one_or_none()

    if download:
        download.file_id = file_id
        download.media_type = media_type
        download.created_at = datetime.now()
        download.download_count += 1
        from datetime import timedelta
        download.expires_at = datetime.now() + timedelta(days=30)
    else:
        download = Download(
            instagram_url=instagram_url,
            file_id=file_id,
            media_type=media_type,
        )
        session.add(download)

    await session.commit()
    return download
