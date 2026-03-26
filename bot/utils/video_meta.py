"""Получение метаданных видео через ffprobe"""
import asyncio
import json
import logging

logger = logging.getLogger(__name__)


async def get_video_meta(file_path: str) -> dict:
    """Возвращает {width, height, duration} видео через ffprobe.
    Если ffprobe недоступен — вернёт пустой словарь (не сломает отправку).
    """
    try:
        proc = await asyncio.create_subprocess_exec(
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_streams", "-select_streams", "v:0",
            file_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await asyncio.wait_for(proc.communicate(), timeout=10)

        data = json.loads(stdout)
        stream = data.get("streams", [{}])[0]

        width = stream.get("width")
        height = stream.get("height")

        # длительность может быть в stream или в format
        duration = stream.get("duration")
        if duration:
            duration = int(float(duration))

        result = {}
        if width:
            result["width"] = int(width)
        if height:
            result["height"] = int(height)
        if duration:
            result["duration"] = duration

        logger.info(f"Мета видео: {result}")
        return result

    except Exception as e:
        logger.warning(f"ffprobe не смог прочитать метаданные: {e}")
        return {}
