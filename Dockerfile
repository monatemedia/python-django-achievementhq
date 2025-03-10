# Stage 1: Base build stage
FROM python:3.12-slim AS builder

# Install necessary system packages for building psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
   build-essential \
   python3-dev \
   gcc \
   libpq-dev \
   && rm -rf /var/lib/apt/lists/*

# Create the app directory
RUN mkdir /app

# Set the working directory
WORKDIR /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Install dependencies first for caching benefit
RUN pip install --upgrade pip 
COPY requirements.txt /app/ 
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.12-slim AS production

# Install runtime dependencies for PostgreSQL
RUN apt-get update && apt-get install -y --no-install-recommends \
   libpq5 \
   postgresql-client \
   sudo \
   && rm -rf /var/lib/apt/lists/*

# Create a non-root user and grant permissions
RUN useradd -m -r -d /home/appuser appuser && \
   mkdir -p /app && \
   chown -R appuser:appuser /app

# Ensure non-root user can access psql
RUN ln -s /usr/bin/psql /usr/local/bin/psql && \
   echo "appuser ALL=(ALL) NOPASSWD: /usr/bin/psql" >> /etc/sudoers

# Set the working directory
WORKDIR /app

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application code
COPY --chown=appuser:appuser /achievementhq /app
COPY --chown=appuser:appuser entrypoint.prod.sh /app

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/usr/local/bin:$PATH"

# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 8000 

# Make entry file executable
RUN chmod +x  /app/entrypoint.prod.sh

# Start the application using Gunicorn
CMD ["/app/entrypoint.prod.sh"]
