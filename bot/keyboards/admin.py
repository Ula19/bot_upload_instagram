"""Клавиатуры админ-панели"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_admin_keyboard() -> InlineKeyboardMarkup:
    """Главное меню админки"""
    buttons = [
        [
            InlineKeyboardButton(
                text="📊 Статистика",
                callback_data="admin_stats",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📢 Каналы",
                callback_data="admin_channels",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_channels_keyboard(channels: list | None = None) -> InlineKeyboardMarkup:
    """Клавиатура управления каналами"""
    buttons = []

    # кнопки удаления для каждого канала (если передали)
    if channels:
        for ch in channels:
            buttons.append([
                InlineKeyboardButton(
                    text=f"🗑 Удалить: {ch.title}",
                    callback_data=f"admin_del_{ch.channel_id}",
                ),
            ])

    buttons.append([
        InlineKeyboardButton(
            text="➕ Добавить канал",
            callback_data="admin_add_channel",
        ),
    ])
    buttons.append([
        InlineKeyboardButton(
            text="◀️ Назад",
            callback_data="admin_cancel",
        ),
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_cancel_keyboard() -> InlineKeyboardMarkup:
    """Кнопка отмены"""
    buttons = [
        [
            InlineKeyboardButton(
                text="❌ Отмена",
                callback_data="admin_cancel",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
