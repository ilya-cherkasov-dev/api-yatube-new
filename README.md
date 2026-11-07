# api-yatube-new

REST API для социальной сети Yatube: посты, группы и комментарии.
Доступ к API только по токену, изменять и удалять можно только свой контент.

## Технологии

- Python 3.14
- Django 5.2
- Django REST Framework 3.17
- Аутентификация по токену (`rest_framework.authtoken`)

## Как запустить

1. Клонировать репозиторий и перейти в него:

   ```bash
   git clone https://github.com/ilya-cherkasov-dev/api-yatube-new.git
   cd api-yatube-new
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows
   . venv/Scripts/activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Применить миграции и запустить сервер:

   ```bash
   cd yatube_api
   python manage.py migrate
   python manage.py runserver
   ```

## Эндпоинты

| Метод | Адрес | Действие |
|---|---|---|
| POST | `/api/v1/api-token-auth/` | получить токен по логину и паролю |
| GET, POST | `/api/v1/posts/` | список постов, создать пост |
| GET, PUT, PATCH, DELETE | `/api/v1/posts/{post_id}/` | получить, изменить, удалить пост |
| GET | `/api/v1/groups/` | список групп |
| GET | `/api/v1/groups/{group_id}/` | информация о группе |
| GET, POST | `/api/v1/posts/{post_id}/comments/` | комментарии к посту, создать комментарий |
| GET, PUT, PATCH, DELETE | `/api/v1/posts/{post_id}/comments/{comment_id}/` | получить, изменить, удалить комментарий |

Токен передаётся в заголовке каждого запроса:

```
Authorization: Token <ваш_токен>
```

Пример создания поста:

```json
POST /api/v1/posts/
{
    "text": "Текст нового поста",
    "group": 1
}
```

Без токена API отвечает `401 Unauthorized`, при попытке изменить чужой
пост или комментарий — `403 Forbidden`. Группы доступны только для чтения.

## Тесты

```bash
pytest
```

## Автор

Ilya Cherkasov
