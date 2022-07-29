# Dockerfile based on ubuntu:18.04
FROM ubuntu:18.04

# Apt update and upgrade
RUN apt-get update && apt-get upgrade -y

# Install python3
RUN apt-get install -y python3

# Define Workdir as /app
WORKDIR /app

# Copy src directory to /app
COPY /src .

# Entrypoint to run the app
ENTRYPOINT ["python3", "lint.py"]