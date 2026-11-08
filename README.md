# Software Architecture & Cloud: Containerization Labs

Hands-on lab repository for the **Software Architecture & Cloud / IoT Systems** course (FH OÖ, Campus Hagenberg & Wels).

This repository contains ready-to-run source code, `Dockerfile` configurations, and step-by-step instructions for all hands-on exercises covered in **Chapter 7 (Cloud & Containerization)**.

---

## ⚡ Fast-Track: Pre-Pull Images at Home (Slow Wi-Fi Survival Guide)

> **Important for FH On-Campus Lectures:**  
> Campus Wi-Fi bandwidth can become congested when many students download multi-hundred megabyte images simultaneously.  
> **Please run the following commands once at home with a stable broadband connection.** All images will be stored in your local Docker cache and available offline during class!

### Single Command (Bash / Zsh / macOS / Linux)

Copy and paste this into your terminal:

```bash
docker pull hello-world && \
docker pull alpine:latest && \
docker pull alpine:3.19 && \
docker pull nginx:alpine && \
docker pull nginxinc/nginx-unprivileged:alpine && \
docker pull python:3.12-alpine && \
docker pull python:3.12-slim && \
docker pull golang:1.22-alpine && \
docker pull golang:1.22 && \
docker pull postgres:16-alpine
```

### Windows (PowerShell)

```powershell
"hello-world", "alpine:latest", "alpine:3.19", "nginx:alpine", "nginxinc/nginx-unprivileged:alpine", "python:3.12-alpine", "python:3.12-slim", "golang:1.22-alpine", "golang:1.22", "postgres:16-alpine" | ForEach-Object { docker pull $_ }
```

### Or run the automated helper script:
```bash
chmod +x pull-all-images.sh
./pull-all-images.sh
```

---

## Lab Overview

| Directory | Topic | Key Concepts | Pre-Pulled Image |
| :--- | :--- | :--- | :--- |
| **[`lab01-docker-cli`](./lab01-docker-cli)** | Docker CLI & Verification | Client/daemon architecture, process isolation, namespaces, resource inspection | `hello-world`, `alpine:latest` |
| **[`lab02-bind-mount-live-reload`](./lab02-bind-mount-live-reload)** | Port Mapping & Live-Reload | Host filesystem bind mounts (`-v $(pwd):/path`), Nginx, hot-reloading without restarts | `nginx:alpine` |
| **[`lab03-volume-persistence-guestbook`](./lab03-volume-persistence-guestbook)** | Named Volume Mounts | Docker-managed storage (`docker volume create`), persistence across container deletion | `python:3.12-alpine` |
| **[`lab04-custom-container-hardening`](./lab04-custom-container-hardening)** | Custom Images & Security | `Dockerfile` directives, layer inspection, security introspection, non-root user | `nginx:alpine`, `nginxinc/nginx-unprivileged:alpine` |
| **[`lab05-multistage-build-go`](./lab05-multistage-build-go)** | Multi-Stage Builds | Statically compiled Go binaries, trimming image size by 98% (builder vs. minimal runtime) | `golang:1.22-alpine`, `alpine:3.19`, `golang:1.22` |
| **[`lab06-python-fastapi-service`](./lab06-python-fastapi-service)** | Python FastAPI Bootstrap | Production ASGI template, Pydantic, OpenAPI / Swagger UI, layer cache optimization | `python:3.12-slim` |
| **[`compose-demo`](./compose-demo)** | Multi-Container Coordination | Declarative `compose.yaml`, service dependencies (`depends_on`), isolated bridge network | `postgres:16-alpine`, `nginx:alpine` |

---

## Prerequisites

Before starting, ensure you have a working container runtime:

```bash
# Verify Docker Engine is running
docker version

# Run a quick test container
docker run --rm hello-world
```

Supported local runtimes:
- **Docker Desktop** (macOS, Windows, Linux)
- **OrbStack** (macOS)
- **Rancher Desktop** (macOS, Windows, Linux)
- **Podman Desktop**
