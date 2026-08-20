FROM eclipse-temurin:21-jdk

WORKDIR /app/soap

COPY soap /app/soap

RUN javac -cp "lib/*" src/com/agendeja/soap/*.java

EXPOSE 8088

CMD ["java", "-cp", "lib/*:src", "com.agendeja.soap.Server"]
