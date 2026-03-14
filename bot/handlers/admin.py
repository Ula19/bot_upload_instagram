"""Админ-панель — управление каналами и статистика
Команды:
  /admin — главное меню админки
  Добавить/удалить каналы через inline-кнопки
"""
import logging

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from bot.config import settings
from bot.database import async_session
from bot.database.crud import (
    add_channel,
    get_active_channels,
    get_user_stats,
    remove_channel,
)
from bot.keyboards.admin import (
    get_admin_keyboard,
    get_cancel_keyboard,
    get_channels_keyboard,
)

logger = logging.getLogger(__name__)
router = Router()


def is_admin(user_id: int) -> bool:
    """Проверяет, админ ли юзер"""
    return user_id in settings.admin_id_list


# === FSM для добавления канала (пошаговый ввод) ===

class AddChannelStates(StatesGroup):
    waiting_channel_id = State()
    waiting_title = State()
    waiting_invite_link = State()


# === Команда /admin ===

@router.message(Command("admin"))
async def cmd_admin(message: Message) -> None:
    """Главное меню админки"""
    if not is_admin(message.from_user.id):
        await message.answer("🚫 У тебя нет доступа к админке.")
        return

    await message.answer(
        "🔧 <b>Админ-панель</b>\n\n"
        "Выбери действие:",
        reply_markup=get_admin_keyboard(),
    )


# === Статистика ===

@router.callback_query(F.data == "admin_stats")
async def admin_stats(callback: CallbackQuery) -> None:
    """Показывает статистику"""
    if not is_admin(callback.from_user.id):
        await callback.answer("🚫 Нет доступа")
        return

    async with async_session() as session:
        stats = await get_user_stats(session)

    text = (
        "📊 <b>Статистика бота</b>\n\n"
        f"👥 Всего юзеров: <b>{stats['total_users']}</b>\n"
        f"🆕 За сегодня: <b>{stats['today_users']}</b>\n"
        f"📥 Всего скачиваний: <b>{stats['total_downloads']}</b>\n"
        f"📢 Каналов: <b>{stats['total_channels']}</b>"
    )

    await callback.message.edit_text(
        text, reply_markup=get_admin_keyboard(),
    )
    await callback.answer()


# === Список каналов ===

@router.callback_query(F.data == "admin_channels")
async def admin_channels(callback: CallbackQuery) -> None:
    """Показывает список каналов"""
    if not is_admin(callback.from_user.id):
        await callback.answer("🚫 Нет доступа")
        return

    async with async_session() as session:
        channels = await get_active_channels(session)

    if not channels:
        text = "📢 <b>Каналы</b>\n\nСписок пуст. Добавь канал кнопкой ниже."
    else:
        lines = ["📢 <b>Каналы для подписки:</b>\n"]
        for i, ch in enumerate(channels, 1):
            lines.append(
                f"{i}. <b>{ch.title}</b>\n"
                f"   ID: <code>{ch.channel_id}</code>\n"
                f"   Ссылка: {ch.invite_link}"
            )
        text = "\n".join(lines)

    await callback.message.edit_text(
        text, reply_markup=get_channels_keyboard(channels if channels else None),
    )
    await callback.answer()


# === Добавление канала (FSM) ===

@router.callback_query(F.data == "admin_add_channel")
async def start_add_channel(callback: CallbackQuery, state: FSMContext) -> None:
    """Начало добавления канала"""
    if not is_admin(callback.from_user.id):
        await callback.answer("🚫 Нет доступа")
        return

    await callback.message.edit_text(
        "📢 <b>Добавление канала</b>\n\n"
        "Отправь <b>ID канала</b> (числовой, например <code>-1001234567890</code>)\n\n"
        "💡 Узнать ID: добавь бота @getmyid_bot в канал",
        reply_markup=get_cancel_keyboard(),
    )
    await state.set_state(AddChannelStates.waiting_channel_id)
    await callback.answer()


@router.message(AddChannelStates.waiting_channel_id)
async def process_channel_id(message: Message, state: FSMContext) -> None:
    """Получаем ID канала"""
    if not is_admin(message.from_user.id):
        return

    try:
        channel_id = int(message.text.strip())
    except ValueError:
        await message.answer(
            "❌ ID должен быть числом. Попробуй ещё раз:",
            reply_markup=get_cancel_keyboard(),
        )
        return

    await state.update_data(channel_id=channel_id)
    await message.answer(
        "✏️ Теперь отправь <b>название канала</b> (для отображения юзеру):",
        reply_markup=get_cancel_keyboard(),
    )
    await state.set_state(AddChannelStates.waiting_title)


@router.message(AddChannelStates.waiting_title)
async def process_title(message: Message, state: FSMContext) -> None:
    """Получаем название"""
    if not is_admin(message.from_user.id):
        return

    title = message.text.strip()
    if len(title) > 200:
        await message.answer("❌ Название слишком длинное (макс 200 символов)")
        return

    await state.update_data(title=title)
    await message.answer(
        "🔗 Теперь отправь <b>ссылку на канал</b> "
        "(например <code>https://t.me/your_channel</code>):",
        reply_markup=get_cancel_keyboard(),
    )
    await state.set_state(AddChannelStates.waiting_invite_link)


@router.message(AddChannelStates.waiting_invite_link)
async def process_invite_link(message: Message, state: FSMContext) -> None:
    """Получаем ссылку и сохраняем канал"""
    if not is_admin(message.from_user.id):
        return

    invite_link = message.text.strip()
    if not invite_link.startswith(("https://t.me/", "https://telegram.me/")):
        await message.answer(
            "❌ Ссылка должна начинаться с https://t.me/\nПопробуй ещё:",
            reply_markup=get_cancel_keyboard(),
        )
        return

    data = await state.get_data()
    await state.clear()

    try:
        async with async_session() as session:
            channel = await add_channel(
                session=session,
                channel_id=data["channel_id"],
                title=data["title"],
                invite_link=invite_link,
            )
        await message.answer(
            f"✅ <b>Канал добавлен!</b>\n\n"
            f"📢 {channel.title}\n"
            f"🆔 <code>{channel.channel_id}</code>\n"
            f"🔗 {channel.invite_link}",
            reply_markup=get_admin_keyboard(),
        )
    except ValueError as e:
        await message.answer(
            f"❌ {e}",
            reply_markup=get_admin_keyboard(),
        )


# === Удаление канала ===

@router.callback_query(F.data.startswith("admin_del_"))
async def delete_channel(callback: CallbackQuery) -> None:
    """Удаление канала по ID"""
    if not is_admin(callback.from_user.id):
        await callback.answer("🚫 Нет доступа")
        return

    channel_id = int(callback.data.replace("admin_del_", ""))

    async with async_session() as session:
        removed = await remove_channel(session, channel_id)

    if removed:
        await callback.answer("✅ Канал удалён!")
    else:
        await callback.answer("❌ Канал не найден")

    # обновляем список
    await admin_channels(callback)


# === Отмена FSM ===

@router.callback_query(F.data == "admin_cancel")
async def cancel_action(callback: CallbackQuery, state: FSMContext) -> None:
    """Отмена текущего действия"""
    await state.clear()
    await callback.message.edit_text(
        "🔧 <b>Админ-панель</b>\n\n"
        "Выбери действие:",
        reply_markup=get_admin_keyboard(),
    )
    await callback.answer("Действие отменено")
