# Dockerfile based on Python
FROM python:3.9-slim

# Create app directory and user
RUN useradd -m app

# Define Workdir as /app
WORKDIR /app
ENV PATH=/home/app/.local/bin:$PATH

# Copy src directory to /app
COPY /src .

# Install python dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Entrypoint to run the app
ENTRYPOINT ["python3", "/app/lint.py"]