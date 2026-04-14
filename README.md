# 🎬 Instagram Downloader Bot

Telegram-бот для скачивания видео, Reels, фото, каруселей и Stories из Instagram.

---

## ✨ Возможности

| Функция | Описание |
|---------|----------|
| 📥 Скачивание | Видео, Reels, фото, карусели (альбомом) и Stories по ссылке |
| 📦 Большие файлы | До 2 ГБ через Local Bot API |
| ⚡ Кэширование | Повторные запросы — мгновенно (file_id, TTL 30 дней) |
| 🌐 Мультиязычность | Русский / Узбекский / English + автоопределение |
| 🔔 Подписка на каналы | Обязательная подписка для использования |
| 🔄 Pending URL | Автоскачивание ссылки после подписки |
| 🚦 Rate limit | 5 запросов в минуту на пользователя |
| 📣 Массовая рассылка | Рассылка по всем юзерам из админки |
| 🔧 Админ-панель | Статистика, управление каналами, рассылка |
| 🎨 UI | Premium custom эмодзи, нативное меню Telegram |

## 🛠 Стек технологий

- **Python 3.12** + **aiogram 3** — асинхронный Telegram Bot API
- **PostgreSQL 16** + **SQLAlchemy 2.0** (async, asyncpg) — база данных
- **Cobalt API** (Docker) — движок скачивания видео/Reels/фото
- **Instagram Private API** — скачивание Stories
- **Telegram Local Bot API** — поддержка файлов до 2 ГБ
- **aiohttp** + **aiohttp-socks** — HTTP-клиент с поддержкой HTTP/HTTPS/SOCKS4/SOCKS5 прокси
- **pydantic-settings** — конфигурация

## 📁 Структура проекта

```
bot_4_insta/
├── bot/
│   ├── config.py              # Настройки из .env
│   ├── i18n.py                # Переводы (ru/uz/en)
│   ├── emojis.py              # Premium custom эмодзи
│   ├── main.py                # Точка входа
│   ├── database/
│   │   ├── __init__.py        # Подключение к БД
│   │   ├── models.py          # User, Channel, Download
│   │   └── crud.py            # CRUD операции
│   ├── handlers/
│   │   ├── start.py           # /start, меню, язык, подписка
│   │   ├── download.py        # Скачивание по ссылке
│   │   └── admin.py           # Админ-панель + рассылка
│   ├── keyboards/
│   │   ├── inline.py          # Основные кнопки
│   │   └── admin.py           # Кнопки админки
│   ├── middlewares/
│   │   ├── rate_limit.py      # 5 запросов в минуту
│   │   └── subscription.py    # Проверка подписки
│   ├── services/
│   │   ├── instagram.py       # Cobalt API клиент
│   │   └── stories.py         # Instagram Stories API (+ SOCKS5)
│   └── utils/
│       └── helpers.py         # URL валидация
├── docker-compose.yml         # Бот + БД + Cobalt + Local Bot API
├── Dockerfile
├── .env.example               # Шаблон переменных
├── requirements.txt           # Зависимости
└── README.md
```

## ⚡ Быстрый старт (Docker Compose)

```bash
# 1. Клонирование
git clone <repo-url> && cd bot_4_insta

# 2. Настройки
cp .env.example .env
# заполнить .env (BOT_TOKEN, ADMIN_IDS, INSTAGRAM_SESSION_ID, API_ID, API_HASH)

# 3. Запуск (поднимает бот, PostgreSQL, Cobalt, Local Bot API)
docker compose up -d --build

# 4. Логи
docker compose logs -f bot

# 5. Обновление
git pull && docker compose up -d --build
```

## 🖥 Локальный запуск (для разработки)

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# нужны внешние сервисы: PostgreSQL + Cobalt
python -m bot.main
```

## ⚙️ Переменные окружения

| Переменная | Описание |
|-----------|----------|
| `BOT_TOKEN` | Токен от @BotFather |
| `ADMIN_IDS` | Telegram ID админов (через запятую) |
| `INSTAGRAM_SESSION_ID` | Cookie sessionid (запасной аккаунт для Stories) |
| `INSTAGRAM_PROXY` | URL прокси (HTTP/HTTPS/SOCKS4/SOCKS5), опционально |
| `COBALT_API_URL` | URL Cobalt API |
| `LOCAL_BOT_API_URL` | URL Local Bot API (для файлов >50 МБ) |
| `API_ID`, `API_HASH` | Telegram API credentials для Local Bot API |
| `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` | Параметры PostgreSQL |
| `CACHE_TTL_DAYS` | TTL кэша скачиваний (по умолчанию 30) |

## 👨‍💻 Админ-панель

Доступ: кнопка «Админ-панель» в меню (только для `ADMIN_IDS`).

- 📊 **Статистика** — юзеры, скачивания, каналы
- 📢 **Каналы** — добавить/удалить каналы обязательной подписки (FSM)
- 📣 **Рассылка** — массовое сообщение всем юзерам (FSM с подтверждением)
- 🏠 **Главное меню** — вернуться в бота

Также приходят алерты при протухании `INSTAGRAM_SESSION_ID`.

## 📄 Лицензия

MIT
