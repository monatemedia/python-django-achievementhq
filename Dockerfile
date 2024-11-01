# Build stage
FROM python:3.12-slim as build

# Upgrade pip and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    build-essential \
    cron && \
    pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy requirements
COPY ./requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project contents from the achievementhq folder to /app
COPY ./achievementhq /app

# Run Django migrations
RUN python manage.py migrate --no-input

# Run Docker Demo
RUN python docker-demo.py --no-input

# Ensure static files can be collected
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Production stage
FROM python:3.12-slim as production

# Install cron in the production stage
RUN apt-get update && \
    apt-get install -y --no-install-recommends cron procps psmisc && \
    rm -rf /var/lib/apt/lists/*  # Clean up APT when done

# Set the working directory
WORKDIR /app

# Copy installed packages, including Gunicorn
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=build /app /app

# Copy static files from build to production stage
COPY --from=build /app/staticfiles /app/staticfiles

# Ensure the demo script is executable
RUN chmod +x /app/docker-demo.py

# Copy the crontab file
COPY crontab.txt /etc/cron.d/my-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/my-cron

# Apply the cron job
RUN crontab /etc/cron.d/my-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Use an entrypoint script to handle migrations and static files
ENTRYPOINT ["sh", "-c", "cron && sleep 10 && tail -f /var/log/cron.log & gunicorn achievementhq.wsgi:application --bind 0.0.0.0:8000"]