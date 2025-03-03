#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python production-demo.py --noinput
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 achievementhq.wsgi:application
