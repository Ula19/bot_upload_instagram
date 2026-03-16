"""Сервис скачивания Instagram Stories — через yt-dlp
yt-dlp умеет скачивать Stories с авторизацией через cookies (sessionid).
"""
import asyncio
import logging
import os
import re
import tempfile

from bot.config import settings

logger = logging.getLogger(__name__)


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


def _create_cookie_file(download_dir: str) -> str:
    """Создаёт Netscape cookies файл с sessionid для yt-dlp"""
    cookie_path = os.path.join(download_dir, "cookies.txt")
    with open(cookie_path, "w") as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write(
            f".instagram.com\tTRUE\t/\tTRUE\t0\tsessionid\t{settings.instagram_session_id}\n"
        )
    return cookie_path


def _download_story_sync(url: str, download_dir: str) -> dict:
    """Синхронная функция скачивания Story через yt-dlp"""
    import yt_dlp

    username, story_id = parse_story_url(url)

    # файл куков для авторизации
    cookie_file = _create_cookie_file(download_dir)

    # шаблон имени файла
    output_template = os.path.join(download_dir, f"story_{username}_{story_id}.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "cookiefile": cookie_file,
        "quiet": True,
        "no_warnings": True,
        "max_filesize": 50 * 1024 * 1024,  # лимит Telegram 50 МБ
        "socket_timeout": 30,
    }

    # если есть прокси — используем
    if settings.instagram_proxy:
        ydl_opts["proxy"] = settings.instagram_proxy

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # определяем путь к скачанному файлу
            if info.get("requested_downloads"):
                file_path = info["requested_downloads"][0]["filepath"]
            else:
                file_path = ydl.prepare_filename(info)

            # определяем тип медиа
            ext = os.path.splitext(file_path)[1].lower()
            if ext in (".mp4", ".webm", ".mkv"):
                media_type = "video"
            else:
                media_type = "photo"

            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            logger.info(f"Story скачана (yt-dlp): {file_path} ({size_mb:.1f} МБ, {media_type})")

            return {
                "file_path": file_path,
                "media_type": media_type,
                "title": f"Story @{username}",
            }
    finally:
        # удаляем файл куков
        if os.path.exists(cookie_file):
            os.remove(cookie_file)


async def download_story(url: str, download_dir: str) -> dict:
    """Асинхронная обёртка — запускает yt-dlp в отдельном потоке"""
    return await asyncio.to_thread(_download_story_sync, url, download_dir)
