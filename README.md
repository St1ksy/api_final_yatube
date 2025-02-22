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
python -m venv venv
```

```
source .venv/bin/activate  # Для Linux/MacOS
. venv/Scripts/activate  # Для Windows
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
python yatube_api/manage.py migrate
```

5. Запустите проект:

```
python yatube_api/manage.py runserver
```
