FROM python:3.11-slim

WORKDIR /app/frontend

COPY frontend /app/frontend

# Usuário sem privilégios; o servidor só lê os arquivos estáticos.
RUN useradd --create-home --uid 1001 app
USER app

EXPOSE 5500

CMD ["python", "-m", "http.server", "5500", "--bind", "0.0.0.0"]
