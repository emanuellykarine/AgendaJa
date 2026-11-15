FROM eclipse-temurin:21-jdk

WORKDIR /app/soap

COPY soap /app/soap

RUN javac -cp "lib/*" src/com/agendeja/soap/*.java

# Usuário sem privilégios; /data é o volume do SQLite compartilhado com o REST (mesmo UID).
RUN useradd --create-home --uid 1001 app \
    && mkdir -p /data && chown app:app /data
USER app

EXPOSE 8088

CMD ["java", "-cp", "lib/*:src", "com.agendeja.soap.Server"]
