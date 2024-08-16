# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables for consistent behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies in a single layer to optimize caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Create a non-root user to run the application
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Specify the command to run the application
CMD ["python", "helloworld.py"]
