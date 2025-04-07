# Yatube API

Yatube — это API-сервис социальной сети, в которой пользователи могут публиковать посты, комментировать их, подписываться друг на друга.

## 🚀 Возможности

- Просмотр и публикация постов
- Комментирование постов
- Работа с группами
- Подписка на пользователей (`/follow/`)
- Аутентификация через JWT

## ⚙️ Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yatube-api.git
   cd yatube-api
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\\Scripts\\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции и запустите сервер:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Документация API будет доступна по адресу:
   ```
   http://127.0.0.1:8000/redoc/
   ```

## 🔐 Аутентификация

Используется JWT:
- `POST /jwt/create/` — получение токена
- `POST /jwt/refresh/` — обновление токена

## 📬 Примеры запросов

### Получение JWT токена
```http
POST /jwt/create/
{
  "username": "your_username",
  "password": "your_password"
}
```

### Подписка на пользователя
```http
POST /api/v1/follow/
Authorization: Bearer <your_token>
{
  "following": "target_username"
}
```

### Получение подписок
```http
GET /api/v1/follow/
Authorization: Bearer <your_token>
```
