"""Клавиатуры бота — кнопки с эмодзи и стилями (Bot API 9.4)"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_start_keyboard() -> InlineKeyboardMarkup:
    """Главное меню после /start"""
    buttons = [
        [
            InlineKeyboardButton(
                text="📥 Скачать видео",
                callback_data="download_video",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📊 Мой профиль",
                callback_data="my_profile",
            ),
            InlineKeyboardButton(
                text="❓ Помощь",
                callback_data="help",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_back_keyboard() -> InlineKeyboardMarkup:
    """Кнопка 'Назад' в главное меню"""
    buttons = [
        [
            InlineKeyboardButton(
                text="◀️ Назад",
                callback_data="back_to_menu",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_subscription_keyboard(
    channels: list[dict],
) -> InlineKeyboardMarkup:
    """Кнопки подписки на каналы + проверка"""
    buttons = []
    for ch in channels:
        buttons.append([
            InlineKeyboardButton(
                text=f"🔔 {ch['title']}",
                url=ch["invite_link"],
            ),
        ])
    # кнопка проверки подписки
    buttons.append([
        InlineKeyboardButton(
            text="✅ Проверить подписку",
            callback_data="check_subscription",
        ),
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
