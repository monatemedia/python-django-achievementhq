#!/bin/sh

# Wait for the database to be ready
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi

# Run Django migrations
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input

# Run docker-demo.py
python docker-demo.py

# Start the Gunicorn server
exec gunicorn achievementhq.wsgi:application --bind 0.0.0.0:8000