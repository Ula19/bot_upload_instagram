# 🎬 Instagram Downloader Bot

Telegram-бот для скачивания видео и фото из Instagram.

## Возможности
- 📥 Скачивание видео, Reels, фото по ссылке
- ⚡ Умное кэширование (повторные запросы — мгновенно)
- 🔔 Обязательная подписка на каналы
- 🎨 Цветные кнопки с эмодзи (Bot API 9.4)
- 🛠 Админ-панель

## Установка

```bash
# Виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# Зависимости
pip install -r requirements.txt

# Настройки
cp .env.example .env
# заполнить .env своими данными

# Создать БД
createdb bot_4_insta

# Запуск
python -m bot.main
```

## Стек
- Python 3.12 + aiogram 3
- PostgreSQL + SQLAlchemy 2.0
- yt-dlp
