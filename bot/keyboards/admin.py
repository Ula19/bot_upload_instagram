"""Клавиатуры админ-панели"""
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.emojis import E_ID
from bot.i18n import t


def get_admin_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Главное меню админки"""
    buttons = [
        [
            InlineKeyboardButton(
                text=t("btn.admin_stats", lang),
                callback_data="admin_stats",
                icon_custom_emoji_id=E_ID["chart"],
            ),
        ],
        [
            InlineKeyboardButton(
                text=t("btn.admin_channels", lang),
                callback_data="admin_channels",
                icon_custom_emoji_id=E_ID["megaphone"],
            ),
        ],
        [
            InlineKeyboardButton(
                text=t("btn.admin_broadcast", lang),
                callback_data="admin_broadcast",
                icon_custom_emoji_id=E_ID["plane"],
            ),
        ],
        [
            InlineKeyboardButton(
                text=t("btn.admin_home", lang),
                callback_data="back_to_menu",
                icon_custom_emoji_id=E_ID["home"],
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_channels_keyboard(
    channels: list | None = None, lang: str = "ru"
) -> InlineKeyboardMarkup:
    """Клавиатура управления каналами"""
    buttons = []

    if channels:
        for ch in channels:
            buttons.append([
                InlineKeyboardButton(
                    text=f"🗑 {ch.title}",
                    callback_data=f"admin_del_{ch.channel_id}",
                    icon_custom_emoji_id=E_ID["trash"],
                ),
            ])

    buttons.append([
        InlineKeyboardButton(
            text=t("btn.admin_add", lang),
            callback_data="admin_add_channel",
            icon_custom_emoji_id=E_ID["plus"],
        ),
    ])
    buttons.append([
        InlineKeyboardButton(
            text=t("btn.admin_back", lang),
            callback_data="admin_cancel",
            icon_custom_emoji_id=E_ID["back"],
        ),
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_cancel_keyboard(lang: str = "ru") -> InlineKeyboardMarkup:
    """Кнопка отмены"""
    buttons = [
        [
            InlineKeyboardButton(
                text=t("btn.admin_cancel", lang),
                callback_data="admin_cancel",
                icon_custom_emoji_id=E_ID["cross"],
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
