FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Usuário sem privilégios.
RUN useradd --create-home --uid 1001 app
COPY --chown=app:app gateway /app/gateway
USER app

WORKDIR /app/gateway

CMD ["python", "mq/consumer.py"]
