#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py create_superuser_if_not_exists
python manage.py create_users
python manage.py create_posts
python manage.py create_comments
python manage.py populate_questions
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 achievementhq.wsgi:application
