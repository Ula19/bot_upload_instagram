# 🚀 Деплой Instagram Bot

## Требования к серверу

- **ОС:** Ubuntu 22.04+ / Debian 12+
- **RAM:** 1 ГБ минимум
- **Python:** 3.11+
- **PostgreSQL:** 14+
- **Docker:** (для Cobalt API)

---

## 1. Установка зависимостей на сервере

```bash
# обновляем систему
sudo apt update && sudo apt upgrade -y

# Python 3.11+
sudo apt install -y python3 python3-pip python3-venv

# PostgreSQL
sudo apt install -y postgresql postgresql-contrib

# Docker (для Cobalt API)
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

## 2. Настройка PostgreSQL

```bash
# создаём юзера и базу
sudo -u postgres psql -c "CREATE USER insta_bot WITH PASSWORD 'your_strong_password';"
sudo -u postgres psql -c "CREATE DATABASE insta_bot_db OWNER insta_bot;"
```

## 3. Клонирование проекта

```bash
cd /opt
git clone <your-repo-url> bot_4_insta
cd bot_4_insta

# создаём виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# устанавливаем зависимости
pip install -r requirements.txt
```

## 4. Настройка .env

```bash
cp .env.example .env
nano .env
```

Заполни каждое поле:

```env
BOT_TOKEN=<токен от @BotFather>
INSTAGRAM_SESSION_ID=<sessionid куки из Instagram>

DB_HOST=localhost
DB_PORT=5432
DB_NAME=insta_bot_db
DB_USER=insta_bot
DB_PASSWORD=your_strong_password

ADMIN_IDS=123456789
COBALT_API_URL=http://localhost:9000
```

### Как получить INSTAGRAM_SESSION_ID:
1. Залогинься в Instagram через браузер (используй **запасной аккаунт**)
2. Открой DevTools (F12) → Application → Cookies → instagram.com
3. Скопируй значение куки `sessionid`

## 5. Запуск Cobalt API (Docker)

```bash
docker run -d \
  --name cobalt \
  --restart unless-stopped \
  -p 9000:9000 \
  -e API_URL=http://localhost:9000 \
  ghcr.io/imputnet/cobalt:10
```

Проверка:
```bash
curl http://localhost:9000
# должен вернуть JSON
```

## 6. Запуск бота (systemd)

Создай сервис:

```bash
sudo nano /etc/systemd/system/insta-bot.service
```

Содержимое:

```ini
[Unit]
Description=Instagram Telegram Bot
After=network.target postgresql.service docker.service

[Service]
Type=simple
User=root
WorkingDirectory=/opt/bot_4_insta
Environment=PATH=/opt/bot_4_insta/venv/bin:/usr/bin
ExecStart=/opt/bot_4_insta/venv/bin/python -m bot.main
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Запуск:

```bash
sudo systemctl daemon-reload
sudo systemctl enable insta-bot
sudo systemctl start insta-bot
```

## 7. Полезные команды

```bash
# статус бота
sudo systemctl status insta-bot

# логи (live)
sudo journalctl -u insta-bot -f

# перезапуск
sudo systemctl restart insta-bot

# остановка
sudo systemctl stop insta-bot

# обновление кода
cd /opt/bot_4_insta
git pull
sudo systemctl restart insta-bot
```

## 8. Чеклист перед запуском

- [ ] PostgreSQL запущен и база создана
- [ ] Docker контейнер Cobalt запущен на порту 9000
- [ ] `.env` заполнен корректно
- [ ] Бот добавлен админом в каналы подписки
- [ ] `ADMIN_IDS` указывает на ваш Telegram ID
- [ ] `INSTAGRAM_SESSION_ID` от **запасного** аккаунта

## 9. Безопасность

⚠️ **Важно:**
- Никогда не коммить `.env` в git
- Используй **запасной аккаунт** Instagram для sessionid
- Ограничь доступ к серверу по SSH ключам
- Регулярно обновляй `sessionid` если бот перестал качать Stories
