# Python parent image
FROM python:3.12-slim

# Check the PATH
RUN echo $PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy requirements.txt from the root folder
COPY requirements.txt /app/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project contents from the achievementhq folder to /app
COPY achievementhq/ /app/

# Remove Pipfile and Pipfile.lock if they exist
RUN rm -f Pipfile Pipfile.lock

# Expose the port (if necessary)
EXPOSE 8000

# Command to run demo.py
CMD ["python", "docker-demo.py"]
