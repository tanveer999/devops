# filepath: /home/tanveer/repo/devops/monitoring/opentelemetry/python-flask/Dockerfile
FROM python:3.12-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Set the default command
CMD ["flask", "run"]