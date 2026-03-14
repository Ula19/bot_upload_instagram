"""Сервис скачивания Instagram — через Cobalt API
Поддерживает: видео, Reels, фото
Cobalt docs: https://github.com/imputnet/cobalt/blob/main/docs/api.md
"""
import asyncio
import logging
import os
import tempfile
from dataclasses import dataclass, field

import aiohttp

from bot.config import settings

logger = logging.getLogger(__name__)


@dataclass
class DownloadResult:
    """Результат скачивания"""
    file_path: str       # путь к файлу
    media_type: str      # video, photo
    title: str           # название
    duration: int | None = None
    thumbnail: str | None = None


@dataclass
class PickerItem:
    """Элемент выбора (для постов с несколькими фото/видео)"""
    url: str
    media_type: str  # photo, video, gif
    thumb: str | None = None


class InstagramDownloader:
    """Скачивает контент из Instagram через Cobalt API"""

    def __init__(self):
        self.download_dir = tempfile.mkdtemp(prefix="insta_bot_")
        self.cobalt_url = settings.cobalt_api_url

    async def download(self, url: str) -> DownloadResult:
        """Скачивает медиа по ссылке Instagram"""
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        body = {"url": url}

        async with aiohttp.ClientSession() as session:
            # запрос к Cobalt API
            async with session.post(
                self.cobalt_url,
                headers=headers,
                json=body,
                timeout=aiohttp.ClientTimeout(total=30),
            ) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    raise RuntimeError(f"Cobalt вернул {resp.status}: {text}")
                data = await resp.json()

            status = data.get("status")
            logger.info(f"Cobalt ответ: status={status}")

            if status == "error":
                error = data.get("error", {})
                raise RuntimeError(
                    f"Cobalt ошибка: {error.get('code', 'unknown')}"
                )

            # redirect — прямая ссылка (видео)
            if status == "redirect":
                media_url = data["url"]
                return await self._download_file(
                    session, media_url, "video",
                    filename=data.get("filename"),
                )

            # tunnel — Cobalt проксирует файл
            if status == "tunnel":
                media_url = data["url"]
                # определяем тип по filename
                filename = data.get("filename", "")
                media_type = self._guess_type(filename)
                return await self._download_file(
                    session, media_url, media_type, filename=filename,
                )

            # picker — несколько элементов (фото-карусель)
            if status == "picker":
                picker = data.get("picker", [])
                if not picker:
                    raise RuntimeError("Cobalt вернул пустой picker")

                # скачиваем первый элемент
                item = picker[0]
                media_type = item.get("type", "photo")
                return await self._download_file(
                    session, item["url"], media_type,
                )

            raise RuntimeError(f"Неизвестный статус Cobalt: {status}")

    async def _download_file(
        self,
        session: aiohttp.ClientSession,
        url: str,
        media_type: str,
        filename: str | None = None,
    ) -> DownloadResult:
        """Скачивает файл по URL"""
        # определяем расширение
        if media_type == "photo":
            ext = ".jpg"
        elif media_type == "gif":
            ext = ".gif"
        else:
            ext = ".mp4"

        if not filename:
            filename = f"insta_{id(url)}{ext}"

        file_path = os.path.join(self.download_dir, filename)

        async with session.get(
            url, timeout=aiohttp.ClientTimeout(total=60)
        ) as resp:
            if resp.status != 200:
                raise RuntimeError(f"Не удалось скачать файл: HTTP {resp.status}")

            content = await resp.read()
            # проверяем размер (лимит Telegram 50 МБ)
            if len(content) > 50 * 1024 * 1024:
                raise RuntimeError("Файл больше 50 МБ — лимит Telegram")

            with open(file_path, "wb") as f:
                f.write(content)

        size_mb = len(content) / (1024 * 1024)
        logger.info(f"Скачано: {file_path} ({size_mb:.1f} МБ, {media_type})")

        return DownloadResult(
            file_path=file_path,
            media_type=media_type,
            title="Instagram",
        )

    def _guess_type(self, filename: str) -> str:
        """Определяет тип медиа по имени файла"""
        lower = filename.lower()
        if any(lower.endswith(e) for e in (".jpg", ".jpeg", ".png", ".webp")):
            return "photo"
        elif lower.endswith(".gif"):
            return "gif"
        return "video"

    def cleanup(self, result: DownloadResult) -> None:
        """Удаляет временные файлы после отправки"""
        try:
            if os.path.exists(result.file_path):
                os.remove(result.file_path)
                logger.info(f"Удалён: {result.file_path}")
        except OSError as e:
            logger.warning(f"Не удалось удалить файл: {e}")


# глобальный экземпляр
downloader = InstagramDownloader()
