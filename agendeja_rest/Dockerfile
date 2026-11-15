FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY agendeja_rest /app/agendeja_rest

# Usuário sem privilégios; /data é o volume do SQLite compartilhado com o SOAP (mesmo UID).
RUN useradd --create-home --uid 1001 app
RUN mkdir -p /data && chown app:app /data
USER app

WORKDIR /app/agendeja_rest

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
