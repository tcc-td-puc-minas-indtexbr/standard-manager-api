#!/bin/sh
python manage.py makemigrations --noinput
python manage.py migrate
#python manage.py migrate &>/dev/null
python manage.py runserver 0.0.0.0:8000

#exec "$@"