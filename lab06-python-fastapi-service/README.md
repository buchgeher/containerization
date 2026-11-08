# Lab 6: Bootstrapping a Python FastAPI Cloud Microservice

This lab provides the canonical, production-ready starting point for building, containerizing, and running **Python FastAPI microservices**.

---

## What is Included?

- **`main.py`**: Modern FastAPI application featuring auto-generated OpenAPI/Swagger documentation, Pydantic type safety, and a `/health` endpoint.
- **`requirements.txt`**: Pinned core dependencies (`fastapi`, `uvicorn`, `pydantic`).
- **`Dockerfile`**: Production-ready containerization with Docker layer caching, `python:3.12-slim`, non-root execution (`USER nobody`), and optimized flags (`PYTHONDONTWRITEBYTECODE=1`, `PYTHONUNBUFFERED=1`).
- **`compose.yaml`**: Optional single-command local development setup with hot-reloading (`--reload` + bind mount).

---

## Step 1: Build the Microservice Image

From this directory (`lab06-python-fastapi-service/`), run:

```bash
docker build -t fastapi-telemetry:v1.0 .
```

> **Docker Layer Caching in action:**  
> Notice that `requirements.txt` is copied and installed **before** `main.py`. When you change code in `main.py`, Docker reuses the cached dependencies and rebuilds in less than a second!

---

## Step 2: Run the Container

```bash
docker run -d --name telemetry-api -p 8000:8000 fastapi-telemetry:v1.0
```

---

## Step 3: Test Endpoints & Explore Interactive Docs

1. **Root Status:**
   ```bash
   curl http://localhost:8000
   ```

2. **Health Check Probe:**
   ```bash
   curl http://localhost:8000/health
   ```

3. **Post Telemetry Data:**
   ```bash
   curl -X POST http://localhost:8000/api/v1/telemetry \
     -H "Content-Type: application/json" \
     -d '{"robot_id": "turtlebot-04", "battery_level": 87.5, "status": "patrolling", "speed_mps": 0.45}'
   ```

4. **Interactive OpenAPI / Swagger UI:**  
   Open **`http://localhost:8000/docs`** in your browser!  
   FastAPI automatically provides interactive API testing and live documentation out of the box.

---

## Step 4: Local Development Mode with Hot-Reloading

For day-to-day coding, use Docker Compose with live code syncing:

```bash
# Start with live reloading enabled
docker compose up -d

# Edit main.py on your machine -> Uvicorn automatically detects changes!

# Teardown
docker compose down
```

---

## Cleanup

```bash
docker stop telemetry-api && docker rm telemetry-api
```

