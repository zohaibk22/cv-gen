# web/Dockerfile
FROM python:3.12-slim

WORKDIR /app

# system deps for psycopg (binary avoids building libpq)
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-traditional \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .