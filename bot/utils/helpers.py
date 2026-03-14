"""Утилиты и вспомогательные функции"""
import re


def is_instagram_url(text: str) -> bool:
    """Проверяет, является ли текст ссылкой на Instagram"""
    pattern = r"https?://(www\.)?(instagram\.com|instagr\.am)/(p|reel|reels|stories|tv)/[\w\-]+"
    return bool(re.match(pattern, text.strip()))


def clean_instagram_url(url: str) -> str:
    """Очищает URL от лишних параметров (utm, igsh и т.д.)"""
    # убираем query параметры
    clean = url.split("?")[0]
    # убираем trailing slash
    return clean.rstrip("/")
