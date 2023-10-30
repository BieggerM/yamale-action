# Dockerfile based on python:3.9-slim-buster
FROM python:3.9-slim-buster

# Create app directory
WORKDIR /app

# Create a group and user
RUN addgroup --system app && adduser --system --group app

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy src directory to /app
COPY /src .

# Change to non-root user
USER app

# Entrypoint to run the app
ENTRYPOINT ["python3", "/app/lint.py"]