# Пульт охраны банка

Веб-приложение позволяет получать информацию из удаленной базы данных
о всех картах доступа в хранилище, сотрудниках находящихся там в данный момент
и истории посещения.

## Как установить

Убедитесь что в системе установлен интерпретатор языка Python 3.5+. 
```
python3 --version
```
Рекомендуется использовать [виртуальное окружение](https://docs.python.org/3/library/venv.html).
```
python3 -m venv env
source env/bin/activate # Unix
.\venv\Scripts\activate # Windows
```

Скачайте [архив](https://github.com/6f6e69/security-console/archive/refs/heads/main.zip) с файлами проекта и разархивируйте в рабочую директорию.

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей. 
```
pip install -r requirements.txt
```
Создайте в рабочей директории файл `.env` и укажите в нем параметры подключения к базе данных
и отключите отладку.

```
DB_ENGINE=django.db.backends.postgresql_psycopg2    # бэкенд базы данных
DB_HOST=bd.bdhost.xyz                               # адрес кластера баз данных
DB_PORT=5432                                        # порт подключения
DB_NAME=security                                    # имя базы данных
DB_USER=user                                        # пользователь
DB_PASSWD=Pa$$wd                                    # пароль
DJANGO_DEBUG=False                                  # отключение отладки
SECRET_KEY=replaceme                                # ОБЯЗАТЕЛЬНО УСТАНОВИТЕ СВОЙ КЛЮЧ
DJANGO_ALLOWED_HOSTS=localhost                      # перечень доменных имен вашего сайта
```

## Запуск

Выполните в консоли команду:
```
$python3 manage.py runserver 0.0.0.0:8000
```

Откройте [ссылку](http://localhost:8000/) в вашем браузере.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).