# Установка проекта без make

Для утановки проекта без make необходимо

запустить терминал windows от имени администратора, перейти в корневую директории проекта и поочередно исполнить команды

![power shell](https://github.com/kiselevvn/legal-service/blob/main/assets/img/cmd-admin.PNG?raw=true)

```cmd
poetry run pip install -U setuptools
poetry install --no-root
```

Создайте файл .env в корне проекта

Содержимое фала
```
DEBUG=true
SITE_DOMAIN="*"
SECRET_KEY=""
DATABASE_URL=sqlite:///public/db.sqlite3
```


```cmd
poetry run task migrate
poetry run task manage createadmin
```
