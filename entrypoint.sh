#!/bin/sh
set -e

# Run migrations
python manage.py migrate --noinput

# Run docker demo
python docker-demo.py

# Start cron
cron && sleep 10

# Start Gunicorn
gunicorn achievementhq.wsgi:application --bind 0.0.0.0:8000
