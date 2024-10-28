# Python parent image
FROM python:3.12-slim

# Upgrade pip
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

# Ensure static files can be collected
RUN mkdir -p /app/staticfiles

# Entry point script
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "sh", "/entrypoint.sh" ]

# Expose the port (if necessary)
EXPOSE 8000

