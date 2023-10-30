# Dockerfile based on alpine/3.6
FROM alpine:3.18

# Install python3
RUN apk add --no-cache bash python3 py3-pip \
  && mkdir -p /app \
  && addgroup -g 10000 app \
  && adduser  -s /bin/bash -G app -u 10000 -h /app -k /dev/null -D app \
  && python3 -m venv /app/venv \
  && chown -R app:app /app

# Define Workdir as /app
WORKDIR /app
ENV VIRTUAL_ENV=/app/venv \
    PATH=/app/venv/bin:$PATH

# Copy src directory to /app
COPY /src .

# Install python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Entrypoint to run the app
ENTRYPOINT ["python3", "/app/lint.py"]