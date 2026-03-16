"""Сервис скачивания Instagram Stories — через instaloader
Instaloader сам управляет сессиями и обходит rate-limit.
Требует логин/пароль Instagram-аккаунта в .env
"""
import asyncio
import logging
import os
import re

import instaloader

from bot.config import settings

logger = logging.getLogger(__name__)

# глобальный экземпляр instaloader (с залогиненной сессией)
_loader: instaloader.Instaloader | None = None


def _get_loader() -> instaloader.Instaloader:
    """Создаёт и логинит instaloader (один раз)"""
    global _loader
    if _loader is not None:
        return _loader

    L = instaloader.Instaloader(
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        compress_json=False,
    )

    # пробуем загрузить сохранённую сессию
    username = settings.instagram_username
    try:
        L.load_session_from_file(username)
        logger.info(f"Instaloader: сессия загружена для @{username}")
    except FileNotFoundError:
        # сессии нет — логинимся
        logger.info(f"Instaloader: логинимся как @{username}...")
        L.login(username, settings.instagram_password)
        L.save_session_to_file()
        logger.info(f"Instaloader: сессия сохранена для @{username}")

    _loader = L
    return _loader


def parse_story_url(url: str) -> tuple[str, str]:
    """Извлекает username и story_id из URL истории
    URL формат: https://www.instagram.com/stories/username/story_id/
    """
    match = re.search(r"stories/([^/]+)/(\d+)", url)
    if not match:
        raise ValueError(f"Не удалось распарсить URL истории: {url}")
    return match.group(1), match.group(2)


def is_story_url(url: str) -> bool:
    """Проверяет, является ли URL ссылкой на историю"""
    return bool(re.search(r"instagram\.com/stories/[^/]+/\d+", url))


def _download_story_sync(url: str, download_dir: str) -> dict:
    """Синхронная функция скачивания Story через instaloader"""
    username, story_id = parse_story_url(url)
    L = _get_loader()

    # получаем профиль
    profile = instaloader.Profile.from_username(L.context, username)

    # ищем нужную историю среди всех stories юзера
    stories = L.get_stories(userids=[profile.userid])

    for story in stories:
        for item in story.get_items():
            if str(item.mediaid) == story_id:
                # определяем тип
                if item.is_video:
                    media_type = "video"
                    ext = ".mp4"
                    media_url = item.video_url
                else:
                    media_type = "photo"
                    ext = ".jpg"
                    media_url = item.url

                # скачиваем файл
                file_path = os.path.join(
                    download_dir, f"story_{username}_{story_id}{ext}"
                )

                # скачиваем через requests (из контекста instaloader)
                response = L.context._session.get(media_url, stream=True)
                response.raise_for_status()

                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                logger.info(
                    f"Story скачана: {file_path} ({size_mb:.1f} МБ, {media_type})"
                )

                return {
                    "file_path": file_path,
                    "media_type": media_type,
                    "title": f"Story @{username}",
                }

    raise RuntimeError("История не найдена или уже истекла (24 часа)")


async def download_story(url: str, download_dir: str) -> dict:
    """Асинхронная обёртка — запускает instaloader в отдельном потоке"""
    return await asyncio.to_thread(_download_story_sync, url, download_dir)
