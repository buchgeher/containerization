# Software Architecture & Cloud: Containerization Labs

Hands-on lab repository for the **Software Architecture & Cloud / IoT Systems** course (FH OÖ, Campus Hagenberg & Wels).

This repository contains ready-to-run source code, `Dockerfile` configurations, and step-by-step instructions for all hands-on exercises covered in **Chapter 7 (Cloud & Containerization)**.

---

## Lab Overview

| Directory | Topic | Key Concepts |
| :--- | :--- | :--- |
| **[`lab01-docker-cli`](./lab01-docker-cli)** | Docker CLI & Verification | Client/daemon architecture, process isolation, namespaces, resource introspection |
| **[`lab02-bind-mount-live-reload`](./lab02-bind-mount-live-reload)** | Port Mapping & Live-Reload | Host filesystem bind mounts (`-v $(pwd):/path`), Nginx, hot-reloading without container restarts |
| **[`lab03-volume-persistence-guestbook`](./lab03-volume-persistence-guestbook)** | Named Volume Mounts | Docker-managed storage (`docker volume create`), persistence across container deletion, guestbook form app |
| **[`lab04-custom-container-hardening`](./lab04-custom-container-hardening)** | Custom Images & Security | `Dockerfile` directives, layer inspection, security introspection (the root problem), unprivileged `USER` non-root hardening |
| **[`lab05-multistage-build-go`](./lab05-multistage-build-go)** | Multi-Stage Builds | Compiling Go binaries without local tools, trimming image size by 98% (builder stage vs. minimal runtime) |
| **[`compose-demo`](./compose-demo)** | Multi-Container Coordination | Declarative `compose.yaml`, service dependencies (`depends_on`), automatic virtual networks, persistent volumes |

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

