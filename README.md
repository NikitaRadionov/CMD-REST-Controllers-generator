# Установка
1. В директории gencode проекта создаем виртуальное окружение
`python -m venv venv`
2. Активируем виртуальное окружение
`venv\Scripts\activate`
3. Собираем cli приложение
`python -m pip install -e .`

# Использование
1. Генерация моделей
```
gencode gen-models --json-schema=C:\Users\User\Desktop\project\json_examples\engine-schema.json --out-dir=C:\Users\User\Desktop\schemas_dir
```

3. Генерация кода REST контроллеров
```
gencode gen-rest --models=C:\Users\User\Desktop\schemas_dir\ --rest-routes=C:\Users\User\Desktop\rest_app
```

# Заметки
1. Для работы REST приложения нужно виртуальное окружение с собственным набором пакетов, которые указаны в файле `requirements_for_app.txt`

2. Также для работы REST приложения нужен `.env` файл на уровне приложений с указанием следующих переменных:
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
База данных Postgres
