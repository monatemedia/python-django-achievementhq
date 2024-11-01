#!/bin/sh
set -e

# Run migrations
python manage.py migrate --noinput

# Start cron
cron && sleep 10

# Start Gunicorn
gunicorn achievementhq.wsgi:application --bind 0.0.0.0:8000
