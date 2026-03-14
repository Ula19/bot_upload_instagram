"""Сервис скачивания Instagram — видео/Reels через yt-dlp
TODO: добавить скачивание фото (Cobalt API или instaloader)
"""
import asyncio
import logging
import os
import tempfile
from dataclasses import dataclass

import yt_dlp

logger = logging.getLogger(__name__)


@dataclass
class DownloadResult:
    """Результат скачивания"""
    file_path: str       # путь к файлу
    media_type: str      # video, photo
    title: str           # название поста
    duration: int | None  # длительность в секундах (для видео)
    thumbnail: str | None  # путь к превью


class InstagramDownloader:
    """Скачивает видео/Reels из Instagram через yt-dlp"""

    def __init__(self):
        self.download_dir = tempfile.mkdtemp(prefix="insta_bot_")

    def _get_yt_dlp_options(self, output_path: str) -> dict:
        """Настройки yt-dlp для скачивания видео"""
        return {
            "outtmpl": output_path,
            "format": "best[ext=mp4]/best",
            "quiet": True,
            "no_warnings": True,
            "extract_flat": False,
            "max_filesize": 50 * 1024 * 1024,  # лимит Telegram 50 МБ
            "noplaylist": True,
            "writethumbnail": True,
            "socket_timeout": 30,
        }

    async def download(self, url: str) -> DownloadResult:
        """Скачивает видео по ссылке Instagram"""
        output_path = os.path.join(self.download_dir, "%(id)s.%(ext)s")
        opts = self._get_yt_dlp_options(output_path)

        # yt-dlp синхронный — запускаем в отдельном потоке
        loop = asyncio.get_event_loop()
        info = await loop.run_in_executor(None, self._yt_dlp_sync, url, opts)

        # фото-посты yt-dlp не поддерживает
        if info.get("_type") == "playlist" and not info.get("entries"):
            raise FileNotFoundError(
                "Это фото-пост. Пока поддерживаются только видео и Reels."
            )

        file_path = self._find_downloaded_file(info)
        if not file_path or not os.path.exists(file_path):
            raise FileNotFoundError("Файл не найден после скачивания.")

        # определяем тип
        ext = os.path.splitext(file_path)[1].lower()
        media_type = "photo" if ext in (".jpg", ".jpeg", ".png", ".webp") else "video"

        return DownloadResult(
            file_path=file_path,
            media_type=media_type,
            title=info.get("title", "Instagram"),
            duration=info.get("duration"),
            thumbnail=None,
        )

    def _find_downloaded_file(self, info: dict) -> str:
        """Ищет скачанный файл"""
        # способ 1: из requested_downloads
        downloads = info.get("requested_downloads", [])
        if downloads and downloads[0].get("filepath"):
            return downloads[0]["filepath"]

        # способ 2: из id + ext
        video_id = info.get("id", "")
        ext = info.get("ext", "mp4")
        if video_id:
            candidate = os.path.join(self.download_dir, f"{video_id}.{ext}")
            if os.path.exists(candidate):
                return candidate

        # способ 3: самый новый файл в папке
        files = []
        for f in os.listdir(self.download_dir):
            full = os.path.join(self.download_dir, f)
            if os.path.isfile(full) and not f.endswith((".json", ".txt")):
                files.append((os.path.getmtime(full), full))

        if files:
            files.sort(reverse=True)
            return files[0][1]

        return ""

    def _yt_dlp_sync(self, url: str, opts: dict) -> dict:
        """Синхронная обёртка yt-dlp"""
        with yt_dlp.YoutubeDL(opts) as ydl:
            return ydl.extract_info(url, download=True)

    def cleanup(self, result: DownloadResult) -> None:
        """Удаляет временные файлы после отправки"""
        try:
            if os.path.exists(result.file_path):
                os.remove(result.file_path)
                logger.info(f"Удалён: {result.file_path}")
            if result.thumbnail and os.path.exists(result.thumbnail):
                os.remove(result.thumbnail)
        except OSError as e:
            logger.warning(f"Не удалось удалить файл: {e}")


# глобальный экземпляр
downloader = InstagramDownloader()
