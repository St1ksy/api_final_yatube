# Проект API для Yatube
Проект представляет собой социальную сеть с функциями публикаций, комментариев, групп и подписок, реализованных через API.

# Как запустить проект?

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/St1ksy/api_final_yatube.git
```

```
cd api_final_yatube
```

2. Создайте и активируйте виртуальное окружение:

```
python3 -m venv .venv
```

```
source .venv/bin/activate  # Для Linux/MacOS
.venv\Scripts\activate  # Для Windows
```

3. Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Выполните миграции:

```
python manage.py migrate
```

5. Запустите проект:

```
python manage.py runserver
```

# Примеры запросов:

- Получение постов постранично
```
GET /api/v1/posts/?limit=10&offset=10
```

- Получение всех комменатриев

```
GET /api/v1/posts/{post_id}/comments/
```

- Удаление комментария

```
DEL /api/v1/posts/{post_id}/comments/{comment_id}/
```

- Публикация поста
```
POST /api/v1/posts/
{
    "text": "string"
}
```

P.S. Все доступные запросы можно увидеть в документации по адресу /redoc/.
