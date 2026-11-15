FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Usuário sem privilégios, dono do código para poder gravar em chat_data/.
RUN useradd --create-home --uid 1001 app
COPY --chown=app:app gateway /app/gateway
USER app

WORKDIR /app/gateway

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
