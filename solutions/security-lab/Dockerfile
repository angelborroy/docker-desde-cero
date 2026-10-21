# syntax=docker/dockerfile:1

# Hardened version of the security lab image (the solution to Dockerfile-2).
# Same application, but it no longer runs as root, has no setuid bash and does
# not install extra network tools. The application still has command injection.
# Non-root limits impact; it does not prove that container escape is impossible.

# Build stage: compiles the app so students do not need Java or Maven installed.
FROM maven:3.10.0-eclipse-temurin-21-noble AS build
WORKDIR /build
COPY pom.xml ./
RUN mvn -q -e dependency:go-offline
COPY src ./src
RUN mvn -q -e clean package -DskipTests

# Runtime stage (hardened)
FROM eclipse-temurin:21.0.12.1_1-jre-noble

COPY flags/root.txt /root/root.txt

# Create and switch to an unprivileged user.
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
USER appuser

COPY --from=build /build/target/cybersecurity-1.0.0.jar app.jar
COPY flags/user.txt /home/factor/user.txt

EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
