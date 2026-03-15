"""Мультиязычность — русский, узбекский, английский
Использование: from bot.i18n import t
  t("start.welcome", lang="en", name="John")
"""

TRANSLATIONS = {
    # === /start ===
    "start.welcome": {
        "ru": (
            "👋 <b>Привет, {name}!</b>\n\n"
            "🎬 Я помогу тебе скачать видео и фото из Instagram.\n\n"
            "📌 <b>Как пользоваться:</b>\n"
            "Просто отправь мне ссылку на пост, Reels или историю — "
            "и я пришлю тебе медиа! 🚀\n\n"
            "Выбери действие ниже:"
        ),
        "uz": (
            "👋 <b>Salom, {name}!</b>\n\n"
            "🎬 Instagram'dan video va rasm yuklab olishda yordam beraman.\n\n"
            "📌 <b>Qanday foydalanish:</b>\n"
            "Menga post, Reels yoki story havolasini yuboring — "
            "men sizga media faylni yuboraman! 🚀\n\n"
            "Quyidagi tugmalardan birini tanlang:"
        ),
        "en": (
            "👋 <b>Hello, {name}!</b>\n\n"
            "🎬 I'll help you download videos and photos from Instagram.\n\n"
            "📌 <b>How to use:</b>\n"
            "Just send me a link to a post, Reels or Story — "
            "and I'll send you the media! 🚀\n\n"
            "Choose an action below:"
        ),
    },

    # === Кнопки главного меню ===
    "btn.download": {
        "ru": "📥 Скачать видео",
        "uz": "📥 Video yuklab olish",
        "en": "📥 Download video",
    },
    "btn.profile": {
        "ru": "📊 Мой профиль",
        "uz": "📊 Mening profilim",
        "en": "📊 My profile",
    },
    "btn.help": {
        "ru": "❓ Помощь",
        "uz": "❓ Yordam",
        "en": "❓ Help",
    },
    "btn.back": {
        "ru": "◀️ Назад",
        "uz": "◀️ Orqaga",
        "en": "◀️ Back",
    },
    "btn.language": {
        "ru": "🌐 Сменить язык",
        "uz": "🌐 Tilni o'zgartirish",
        "en": "🌐 Change language",
    },

    # === Скачивание ===
    "download.prompt": {
        "ru": (
            "📥 <b>Скачивание видео из Instagram</b>\n\n"
            "Отправь мне ссылку на:\n"
            "• Пост (фото/видео)\n"
            "• Reels\n"
            "• Историю\n\n"
            "🔗 Пример: <code>https://www.instagram.com/reel/...</code>"
        ),
        "uz": (
            "📥 <b>Instagram'dan video yuklab olish</b>\n\n"
            "Menga quyidagi havolani yuboring:\n"
            "• Post (rasm/video)\n"
            "• Reels\n"
            "• Story\n\n"
            "🔗 Misol: <code>https://www.instagram.com/reel/...</code>"
        ),
        "en": (
            "📥 <b>Download video from Instagram</b>\n\n"
            "Send me a link to:\n"
            "• Post (photo/video)\n"
            "• Reels\n"
            "• Story\n\n"
            "🔗 Example: <code>https://www.instagram.com/reel/...</code>"
        ),
    },
    "download.processing": {
        "ru": "⏳ Скачиваю... Подожди немного",
        "uz": "⏳ Yuklab olinmoqda... Biroz kuting",
        "en": "⏳ Downloading... Please wait",
    },
    "download.not_instagram": {
        "ru": (
            "🤔 Это не похоже на ссылку Instagram.\n\n"
            "Отправь ссылку вида:\n"
            "<code>https://www.instagram.com/...</code>"
        ),
        "uz": (
            "🤔 Bu Instagram havolasiga o'xshamaydi.\n\n"
            "Quyidagi ko'rinishdagi havolani yuboring:\n"
            "<code>https://www.instagram.com/...</code>"
        ),
        "en": (
            "🤔 This doesn't look like an Instagram link.\n\n"
            "Send a link like:\n"
            "<code>https://www.instagram.com/...</code>"
        ),
    },
    "download.only_video": {
        "ru": "📸 Пока поддерживаются только видео, Reels и Stories.",
        "uz": "📸 Hozircha faqat video, Reels va Stories qo'llab-quvvatlanadi.",
        "en": "📸 Currently only videos, Reels and Stories are supported.",
    },

    # === Профиль ===
    "profile.title": {
        "ru": (
            "👤 <b>Твой профиль</b>\n\n"
            "📛 Имя: {full_name}\n"
            "🆔 ID: <code>{user_id}</code>\n"
            "📥 Скачиваний (всего): {downloads}\n"
        ),
        "uz": (
            "👤 <b>Sizning profilingiz</b>\n\n"
            "📛 Ism: {full_name}\n"
            "🆔 ID: <code>{user_id}</code>\n"
            "📥 Yuklashlar (jami): {downloads}\n"
        ),
        "en": (
            "👤 <b>Your profile</b>\n\n"
            "📛 Name: {full_name}\n"
            "🆔 ID: <code>{user_id}</code>\n"
            "📥 Downloads (total): {downloads}\n"
        ),
    },

    # === Помощь ===
    "help.text": {
        "ru": (
            "❓ <b>Помощь</b>\n\n"
            "🔹 Отправь ссылку на пост Instagram — получишь видео или фото\n"
            "🔹 Поддерживаются: посты, Reels, истории\n"
            "🔹 Приватные аккаунты не поддерживаются\n\n"
            "📩 По вопросам: @{admin_username}"
        ),
        "uz": (
            "❓ <b>Yordam</b>\n\n"
            "🔹 Instagram post havolasini yuboring — video yoki rasm olasiz\n"
            "🔹 Qo'llab-quvvatlanadi: postlar, Reels, stories\n"
            "🔹 Yopiq akkauntlar qo'llab-quvvatlanmaydi\n\n"
            "📩 Savollar uchun: @{admin_username}"
        ),
        "en": (
            "❓ <b>Help</b>\n\n"
            "🔹 Send an Instagram post link — get a video or photo\n"
            "🔹 Supported: posts, Reels, stories\n"
            "🔹 Private accounts are not supported\n\n"
            "📩 Contact: @{admin_username}"
        ),
    },

    # === Подписка ===
    "sub.welcome": {
        "ru": (
            "👋 <b>Привет!</b>\n\n"
            "🎬 Этот бот скачивает видео, фото и Stories "
            "из Instagram — быстро и бесплатно!\n\n"
            "🔒 <b>Для начала подпишись на каналы ниже:</b>\n\n"
            "После подписки нажми «✅ Проверить подписку»"
        ),
        "uz": (
            "👋 <b>Salom!</b>\n\n"
            "🎬 Bu bot Instagram'dan video, rasm va Stories "
            "yuklab oladi — tez va bepul!\n\n"
            "🔒 <b>Boshlash uchun quyidagi kanallarga obuna bo'ling:</b>\n\n"
            "Obuna bo'lgandan keyin «✅ Obunani tekshirish» tugmasini bosing"
        ),
        "en": (
            "👋 <b>Hello!</b>\n\n"
            "🎬 This bot downloads videos, photos and Stories "
            "from Instagram — fast and free!\n\n"
            "🔒 <b>To start, subscribe to the channels below:</b>\n\n"
            "After subscribing, tap «✅ Check subscription»"
        ),
    },
    "sub.not_subscribed": {
        "ru": (
            "❌ <b>Ты ещё не подписался на все каналы:</b>\n\n"
            "Подпишись и нажми «✅ Проверить подписку» ещё раз."
        ),
        "uz": (
            "❌ <b>Siz hali barcha kanallarga obuna bo'lmadingiz:</b>\n\n"
            "Obuna bo'ling va «✅ Obunani tekshirish» tugmasini qayta bosing."
        ),
        "en": (
            "❌ <b>You haven't subscribed to all channels yet:</b>\n\n"
            "Subscribe and tap «✅ Check subscription» again."
        ),
    },
    "sub.success": {
        "ru": (
            "✅ <b>Отлично, {name}!</b>\n\n"
            "Теперь ты можешь пользоваться ботом! 🚀\n\n"
            "Отправь ссылку на пост, Reels или историю Instagram."
        ),
        "uz": (
            "✅ <b>Ajoyib, {name}!</b>\n\n"
            "Endi siz botdan foydalanishingiz mumkin! 🚀\n\n"
            "Instagram post, Reels yoki story havolasini yuboring."
        ),
        "en": (
            "✅ <b>Great, {name}!</b>\n\n"
            "You can now use the bot! 🚀\n\n"
            "Send a link to an Instagram post, Reels or Story."
        ),
    },
    "btn.check_sub": {
        "ru": "✅ Проверить подписку",
        "uz": "✅ Obunani tekshirish",
        "en": "✅ Check subscription",
    },
    "sub.check_alert_fail": {
        "ru": "❌ Подпишись на все каналы!",
        "uz": "❌ Barcha kanallarga obuna bo'ling!",
        "en": "❌ Subscribe to all channels!",
    },
    "sub.check_alert_ok": {
        "ru": "✅ Подписка подтверждена!",
        "uz": "✅ Obuna tasdiqlandi!",
        "en": "✅ Subscription confirmed!",
    },
    "sub.not_required": {
        "ru": "✅ Подписка не требуется!",
        "uz": "✅ Obuna talab qilinmaydi!",
        "en": "✅ No subscription required!",
    },

    # === Ошибки ===
    "error.session": {
        "ru": "🔑 <b>Нужна авторизация</b>\n\nДля скачивания Stories нужен INSTAGRAM_SESSION_ID.",
        "uz": "🔑 <b>Avtorizatsiya kerak</b>\n\nStories yuklab olish uchun INSTAGRAM_SESSION_ID kerak.",
        "en": "🔑 <b>Authorization required</b>\n\nINSTAGRAM_SESSION_ID is needed to download Stories.",
    },
    "error.story_expired": {
        "ru": "⏰ <b>История не найдена</b>\n\nВозможно, она уже истекла (24 часа) или аккаунт приватный.",
        "uz": "⏰ <b>Story topilmadi</b>\n\nEhtimol, u allaqachon o'chirilgan (24 soat) yoki akkaunt yopiq.",
        "en": "⏰ <b>Story not found</b>\n\nIt may have expired (24 hours) or the account is private.",
    },
    "error.private": {
        "ru": "🔒 <b>Аккаунт приватный</b>\n\nК сожалению, скачивание из приватных аккаунтов невозможно.",
        "uz": "🔒 <b>Akkaunt yopiq</b>\n\nAfsuski, yopiq akkauntlardan yuklab olish mumkin emas.",
        "en": "🔒 <b>Private account</b>\n\nUnfortunately, downloading from private accounts is not possible.",
    },
    "error.not_found": {
        "ru": "❌ <b>Пост не найден</b>\n\nВозможно, он удалён или ссылка неправильная.",
        "uz": "❌ <b>Post topilmadi</b>\n\nEhtimol, u o'chirilgan yoki havola noto'g'ri.",
        "en": "❌ <b>Post not found</b>\n\nIt may have been deleted or the link is incorrect.",
    },
    "error.unsupported": {
        "ru": "🚫 <b>Ссылка не поддерживается</b>\n\nПоддерживаются: посты, Reels и Stories.",
        "uz": "🚫 <b>Havola qo'llab-quvvatlanmaydi</b>\n\nQo'llab-quvvatlanadi: postlar, Reels va Stories.",
        "en": "🚫 <b>Link not supported</b>\n\nSupported: posts, Reels and Stories.",
    },
    "error.too_large": {
        "ru": "📦 <b>Файл слишком большой</b>\n\nTelegram ограничивает размер файла до 50 МБ.",
        "uz": "📦 <b>Fayl juda katta</b>\n\nTelegram fayl hajmini 50 MB bilan cheklaydi.",
        "en": "📦 <b>File too large</b>\n\nTelegram limits file size to 50 MB.",
    },
    "error.timeout": {
        "ru": "⏱ <b>Превышено время ожидания</b>\n\nПопробуй ещё раз через пару минут.",
        "uz": "⏱ <b>Kutish vaqti tugadi</b>\n\nBir necha daqiqadan keyin qayta urinib ko'ring.",
        "en": "⏱ <b>Request timed out</b>\n\nPlease try again in a few minutes.",
    },
    "error.generic": {
        "ru": "❌ <b>Не удалось скачать</b>\n\nПопробуй позже или проверь ссылку.",
        "uz": "❌ <b>Yuklab olib bo'lmadi</b>\n\nKeyinroq urinib ko'ring yoki havolani tekshiring.",
        "en": "❌ <b>Download failed</b>\n\nTry again later or check the link.",
    },
    "error.rate_limit": {
        "ru": "⏳ <b>Слишком много запросов!</b>\n\nПодожди {seconds} секунд и попробуй снова.",
        "uz": "⏳ <b>Juda ko'p so'rovlar!</b>\n\n{seconds} soniya kuting va qayta urinib ko'ring.",
        "en": "⏳ <b>Too many requests!</b>\n\nWait {seconds} seconds and try again.",
    },

    # === Выбор языка ===
    "lang.choose": {
        "ru": "🌐 <b>Выберите язык:</b>",
        "uz": "🌐 <b>Tilni tanlang:</b>",
        "en": "🌐 <b>Choose language:</b>",
    },
    "lang.changed": {
        "ru": "✅ Язык изменён на русский",
        "uz": "✅ Til o'zbek tiliga o'zgartirildi",
        "en": "✅ Language changed to English",
    },

    # === Админ-панель ===
    "admin.title": {
        "ru": "🔧 <b>Админ-панель</b>\n\nВыбери действие:",
        "uz": "🔧 <b>Admin panel</b>\n\nAmalni tanlang:",
        "en": "🔧 <b>Admin panel</b>\n\nChoose an action:",
    },
    "admin.no_access": {
        "ru": "🚫 У тебя нет доступа к админке.",
        "uz": "🚫 Sizda admin panelga kirish huquqi yo'q.",
        "en": "🚫 You don't have access to admin panel.",
    },
    "admin.stats": {
        "ru": (
            "📊 <b>Статистика бота</b>\n\n"
            "👥 Всего юзеров: <b>{total_users}</b>\n"
            "🆕 Новых юзеров сегодня: <b>{today_users}</b>\n"
            "📥 Всего скачиваний: <b>{total_downloads}</b>\n"
            "📢 Каналов: <b>{total_channels}</b>"
        ),
        "uz": (
            "📊 <b>Bot statistikasi</b>\n\n"
            "👥 Jami foydalanuvchilar: <b>{total_users}</b>\n"
            "🆕 Bugungi yangi foydalanuvchilar: <b>{today_users}</b>\n"
            "📥 Jami yuklashlar: <b>{total_downloads}</b>\n"
            "📢 Kanallar: <b>{total_channels}</b>"
        ),
        "en": (
            "📊 <b>Bot statistics</b>\n\n"
            "👥 Total users: <b>{total_users}</b>\n"
            "🆕 New users today: <b>{today_users}</b>\n"
            "📥 Total downloads: <b>{total_downloads}</b>\n"
            "📢 Channels: <b>{total_channels}</b>"
        ),
    },
    "admin.channels_empty": {
        "ru": "📢 <b>Каналы</b>\n\nСписок пуст. Добавь канал кнопкой ниже.",
        "uz": "📢 <b>Kanallar</b>\n\nRo'yxat bo'sh. Quyidagi tugma orqali kanal qo'shing.",
        "en": "📢 <b>Channels</b>\n\nList is empty. Add a channel using the button below.",
    },
    "admin.channels_title": {
        "ru": "📢 <b>Каналы для подписки:</b>\n",
        "uz": "📢 <b>Obuna kanallari:</b>\n",
        "en": "📢 <b>Subscription channels:</b>\n",
    },
    "admin.add_channel_id": {
        "ru": (
            "📢 <b>Добавление канала</b>\n\n"
            "Отправь <b>ID канала</b> (числовой, например <code>-1001234567890</code>)\n\n"
            "💡 Узнать ID: добавь бота @getmyid_bot в канал"
        ),
        "uz": (
            "📢 <b>Kanal qo'shish</b>\n\n"
            "<b>Kanal ID</b> raqamini yuboring (masalan <code>-1001234567890</code>)\n\n"
            "💡 ID bilish: @getmyid_bot ni kanalga qo'shing"
        ),
        "en": (
            "📢 <b>Add channel</b>\n\n"
            "Send the <b>channel ID</b> (numeric, e.g. <code>-1001234567890</code>)\n\n"
            "💡 Get ID: add @getmyid_bot to the channel"
        ),
    },
    "admin.add_channel_title": {
        "ru": "✏️ Теперь отправь <b>название канала</b> (для отображения юзеру):",
        "uz": "✏️ Endi <b>kanal nomini</b> yuboring (foydalanuvchiga ko'rsatiladi):",
        "en": "✏️ Now send the <b>channel name</b> (displayed to the user):",
    },
    "admin.add_channel_link": {
        "ru": (
            "🔗 Теперь отправь <b>ссылку или юзернейм канала</b>\n\n"
            "Принимаю любой формат:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
        "uz": (
            "🔗 Endi <b>kanal havolasi yoki username</b> yuboring\n\n"
            "Istalgan formatda:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
        "en": (
            "🔗 Now send the <b>channel link or username</b>\n\n"
            "Any format accepted:\n"
            "• <code>https://t.me/your_channel</code>\n"
            "• <code>@your_channel</code>\n"
            "• <code>your_channel</code>"
        ),
    },
    "admin.channel_added": {
        "ru": "✅ <b>Канал добавлен!</b>",
        "uz": "✅ <b>Kanal qo'shildi!</b>",
        "en": "✅ <b>Channel added!</b>",
    },
    "admin.confirm_delete": {
        "ru": "⚠️ <b>Удалить канал?</b>\n\nID: <code>{channel_id}</code>\n\nЭто действие нельзя отменить.",
        "uz": "⚠️ <b>Kanalni o'chirishni xohlaysizmi?</b>\n\nID: <code>{channel_id}</code>\n\nBu amalni qaytarib bo'lmaydi.",
        "en": "⚠️ <b>Delete channel?</b>\n\nID: <code>{channel_id}</code>\n\nThis action cannot be undone.",
    },
    "admin.id_not_number": {
        "ru": "❌ ID должен быть числом. Попробуй ещё раз:",
        "uz": "❌ ID raqam bo'lishi kerak. Qayta urinib ko'ring:",
        "en": "❌ ID must be a number. Try again:",
    },
    "admin.title_too_long": {
        "ru": "❌ Название слишком длинное (макс 200 символов)",
        "uz": "❌ Nom juda uzun (maks 200 belgi)",
        "en": "❌ Name is too long (max 200 characters)",
    },
    "admin.link_invalid": {
        "ru": "❌ Не удалось распознать ссылку.\nПопробуй ещё:",
        "uz": "❌ Havolani aniqlab bo'lmadi.\nQayta urinib ko'ring:",
        "en": "❌ Could not parse the link.\nTry again:",
    },
    "btn.admin_stats": {
        "ru": "📊 Статистика",
        "uz": "📊 Statistika",
        "en": "📊 Statistics",
    },
    "btn.admin_channels": {
        "ru": "📢 Каналы",
        "uz": "📢 Kanallar",
        "en": "📢 Channels",
    },
    "btn.admin_home": {
        "ru": "🏠 Главное меню",
        "uz": "🏠 Bosh menyu",
        "en": "🏠 Main menu",
    },
    "btn.admin_add": {
        "ru": "➕ Добавить канал",
        "uz": "➕ Kanal qo'shish",
        "en": "➕ Add channel",
    },
    "btn.admin_back": {
        "ru": "◀️ Назад",
        "uz": "◀️ Orqaga",
        "en": "◀️ Back",
    },
    "btn.admin_cancel": {
        "ru": "❌ Отмена",
        "uz": "❌ Bekor qilish",
        "en": "❌ Cancel",
    },
    "btn.admin_confirm_del": {
        "ru": "✅ Да, удалить",
        "uz": "✅ Ha, o'chirish",
        "en": "✅ Yes, delete",
    },
    "btn.admin_cancel_del": {
        "ru": "❌ Отмена",
        "uz": "❌ Bekor qilish",
        "en": "❌ Cancel",
    },
    "btn.admin_panel": {
        "ru": "🔧 Админ-панель",
        "uz": "🔧 Admin panel",
        "en": "🔧 Admin panel",
    },
    "btn.admin_broadcast": {
        "ru": "📨 Рассылка",
        "uz": "📨 Xabar yuborish",
        "en": "📨 Broadcast",
    },
    "admin.broadcast_prompt": {
        "ru": (
            "📨 <b>Массовая рассылка</b>\n\n"
            "Отправь текст/фото/видео для рассылки.\n"
            "Поддерживается HTML-разметка."
        ),
        "uz": (
            "📨 <b>Ommaviy xabar</b>\n\n"
            "Yuborish uchun matn/rasm/video yuboring.\n"
            "HTML formatlash qo'llab-quvvatlanadi."
        ),
        "en": (
            "📨 <b>Mass broadcast</b>\n\n"
            "Send text/photo/video to broadcast.\n"
            "HTML formatting is supported."
        ),
    },
    "admin.broadcast_preview": {
        "ru": "👆 <b>Предпросмотр</b>\n\nОтправить это сообщение всем юзерам?",
        "uz": "👆 <b>Oldindan ko'rish</b>\n\nBu xabarni barcha foydalanuvchilarga yuborishni xohlaysizmi?",
        "en": "👆 <b>Preview</b>\n\nSend this message to all users?",
    },
    "admin.broadcast_confirm": {
        "ru": "✅ Да, отправить",
        "uz": "✅ Ha, yuborish",
        "en": "✅ Yes, send",
    },
    "admin.broadcast_cancel": {
        "ru": "❌ Отмена",
        "uz": "❌ Bekor qilish",
        "en": "❌ Cancel",
    },
    "admin.broadcast_started": {
        "ru": "📨 Рассылка запущена... Ожидай отчёт.",
        "uz": "📨 Xabar yuborilmoqda... Hisobotni kuting.",
        "en": "📨 Broadcast started... Wait for report.",
    },
    "admin.broadcast_done": {
        "ru": (
            "📊 <b>Рассылка завершена!</b>\n\n"
            "✅ Доставлено: <b>{success}</b>\n"
            "❌ Ошибок: <b>{failed}</b>\n"
            "👥 Всего: <b>{total}</b>"
        ),
        "uz": (
            "📊 <b>Xabar yuborish tugadi!</b>\n\n"
            "✅ Yetkazildi: <b>{success}</b>\n"
            "❌ Xatolar: <b>{failed}</b>\n"
            "👥 Jami: <b>{total}</b>"
        ),
        "en": (
            "📊 <b>Broadcast complete!</b>\n\n"
            "✅ Delivered: <b>{success}</b>\n"
            "❌ Failed: <b>{failed}</b>\n"
            "👥 Total: <b>{total}</b>"
        ),
    },
}


def t(key: str, lang: str = "ru", **kwargs) -> str:
    """Получить перевод по ключу и языку"""
    translations = TRANSLATIONS.get(key, {})
    text = translations.get(lang, translations.get("en", f"[{key}]"))
    if kwargs:
        text = text.format(**kwargs)
    return text


def detect_language(language_code: str | None) -> str:
    """Определяет язык по Telegram: ru → русский, uz → узбекский, остальное → английский"""
    if not language_code:
        return "en"
    if language_code.startswith("ru"):
        return "ru"
    if language_code.startswith("uz"):
        return "uz"
    return "en"
