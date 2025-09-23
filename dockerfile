# web/Dockerfile
FROM python:3.12-slim

WORKDIR /app

# system deps for psycopg and WeasyPrint
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-traditional \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libcairo-gobject2 \
    libgtk-3-0 \
    libglib2.0-0 \
    libfontconfig1 \
    fonts-liberation \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .