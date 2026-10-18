# DOCKER-COUNTER
# Docker Counter App

A Flask application that counts page visits and stores the count in a Docker volume.

## Skills practised
- Building Docker images using a Dockerfile
- Running containers and mapping ports
- Persisting data using Docker volumes
- Checking container logs and application health

## Run the application

```bash
docker build -t counter-app:v1 .
docker volume create counter-data
docker run -d --name counter-container -p 8080:5000 -v counter-data:/app/data counter-app:v1
```

Open http://localhost:8080.

Health endpoint: http://localhost:8080/health.

## Test persistence

Stop and remove the container, then recreate it using the same volume.
The saved counter continues from its previous value.

## Limitations

This project is for local learning. It uses Flask's development server
and a simple file counter intended for one visitor at a time.
