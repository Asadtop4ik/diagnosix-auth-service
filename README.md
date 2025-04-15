# Diagnosix Auth-Service

Микросервис аутентификации (auth-service) для проекта Diagnosix. Этот сервис предназначен для регистрации пользователей, аутентификации и предоставления информации о пользователях с использованием JWT-токенов.

## О проекте

Этот проект представляет собой REST API, созданный с использованием фреймворка FastAPI. Он поддерживает следующие функции:

- Регистрация пользователей (`/register`).
- Аутентификация пользователей (`/login`).
- Управление ролями пользователей (`patient`, `doctor`, `admin`) через JWT-токены.
- Получение информации о пользователе (`/me`).

### Технологии

- **FastAPI**: Для создания REST API.
- **PostgreSQL**: В качестве базы данных.
- **Alembic**: Для миграций базы данных.
- **Pydantic**: Для валидации и сериализации данных.
- **JWT**: Для аутентификации (используется библиотека `python-jose`).
- **Docker & Docker Compose**: Для контейнеризации проекта.
- **Pytest**: Для юнит-тестов.

### Безопасность

- Пароли хешируются с использованием `bcrypt`.
- JWT-токены создаются с алгоритмом `HS256`.
- Роли пользователей (`patient`, `doctor`, `admin`) определены как перечисления (enum) и хранятся в базе данных.

## Структура проекта

```
diagnosix-auth-service/
├── app/
│   ├── __init__.py
│   ├── auth.py          # Логика аутентификации (хеширование паролей, JWT-токены)
│   ├── auth_routes.py   # Эндпоинты API
│   ├── config.py        # Настройки (DATABASE_URL, JWT_SECRET_KEY и др.)
│   ├── database.py      # Настройки базы данных
│   ├── main.py          # Приложение FastAPI
│   ├── models.py        # Модели SQLAlchemy
│   ├── schemas.py       # Модели Pydantic
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # Общие настройки для тестов
│   ├── test_auth.py     # Тесты для auth.py
│   ├── test_auth_routes.py  # Тесты для auth_routes.py
├── alembic/             # Миграции Alembic
├── Dockerfile           # Для создания Docker-образа
├── docker-compose.yml   # Настройки Docker Compose
├── requirements.txt     # Зависимости проекта
├── .env                 # Переменные окружения
├── pytest.ini           # Настройки Pytest
└── README.md            # Документация проекта
```

## Установка и запуск

### Требования

- Python 3.12+
- Docker и Docker Compose
- Git

### 1. Клонирование проекта

```bash
git clone https://github.com/<your-username>/diagnosix-auth-service.git
cd diagnosix-auth-service
```

### 2. Настройка переменных окружения

Создайте файл `.env` и добавьте следующие переменные:

```env
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=db
DATABASE_URL=postgresql://username:password@db:5432/db
JWT_SECRET_KEY=secret_key
JWT_ALGORITHM=HS256
```

### 3. Установка зависимостей (без Docker)

Если вы хотите запустить проект без Docker, создайте виртуальное окружение и установите зависимости:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Запуск с помощью Docker

Самый простой способ запустить проект — использовать Docker Compose:

```bash
sudo docker compose up --build
```

Это запустит следующие сервисы:
- `auth-service`: Приложение FastAPI (доступно по адресу `http://localhost:8000`).
- `db`: База данных PostgreSQL.
- `migration`: Для применения миграций Alembic.

Чтобы просмотреть документацию Swagger, откройте в браузере `http://localhost:8000/docs`.

### 5. Запуск тестов

Для запуска юнит-тестов выполните:

```bash
pytest -v
```

Или внутри Docker:

```bash
sudo docker compose run test
```

## Эндпоинты API и примеры запросов (curl)

### 1. Регистрация пользователя (`/auth/register`)

**Запрос**:
```bash
curl -X POST http://localhost:8000/auth/register \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass", "role": "patient"}'
```

**Ответ**:
```json
{
  "id": 1,
  "username": "testuser",
  "role": "patient"
}
```

### 2. Аутентификация пользователя (`/auth/login`)

**Запрос**:
```bash
curl -X POST http://localhost:8000/auth/login \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass"}'
```

**Ответ**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Получение информации о пользователе (`/auth/me`)

**Запрос**:
```bash
curl http://localhost:8000/auth/me \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Ответ**:
```json
{
  "id": 1,
  "username": "testuser",
  "role": "patient"
}
```

## Тесты

Для проекта написаны юнит-тесты для следующих эндпоинтов и функций:
- `/register`: Регистрация нового пользователя, регистрация с существующим пользователем, неверная роль, пустые `username` и `password`.
- `/login`: Успешный вход и вход с неверными данными.
- `/me`: Получение информации о пользователе, включая запрос с истёкшим токеном.
- Функции в `auth.py`: Хеширование пароля, проверка пароля, создание и декодирование JWT-токенов.


## Автор

- **Имя**: Асадбек
- **Контакт**: [asadbek.backend.com]
- **GitHub**: [github.com/Asadtop4ik] 
```
