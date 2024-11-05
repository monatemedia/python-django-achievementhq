#!/bin/sh
set -e

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Run docker demo
echo "Running demo script..."
python docker-demo.py

# Start cron in the background
echo "Starting cron..."
cron && sleep 10

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn achievementhq.wsgi:application --bind 0.0.0.0:8000
