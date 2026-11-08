# Lab 1: Docker Commands & Local Environment

In this lab, you verify your Docker installation, inspect the client/daemon separation, run lightweight containers, and learn essential management commands.

---

## Hands-on Exercises

### Step 1: Verify Engine & System Info

```bash
# Check client and server daemon version
docker version

# Display system-wide information (storage driver, CPU/RAM, active runtimes)
docker info
```

### Step 2: Hello World & Execution Flags

```bash
# Pull and run the canonical verification image
docker run hello-world

# Run an ephemeral container that cleans up after exit (--rm)
# NOTE: Use single quotes to prevent zsh history expansion issues with '!'
docker run --rm alpine echo 'Hello from isolated Alpine container!'
```

### Step 3: Container Inspection & Namespaces

```bash
# Run a background (detached) container
docker run -d --name test-box alpine sleep 300

# List active containers
docker ps

# Inspect low-level JSON configuration (IP address, mounts, environment)
docker inspect test-box

# Stop and remove the container
docker stop test-box && docker rm test-box
```

---

## Docker CLI Cheat Sheet: Everyday Essentials

### 1. Container Lifecycle
| Command | Description |
| :--- | :--- |
| `docker run -d --name <n> -p 8080:80 <img>` | Run detached container with port forwarding |
| `docker run --rm -it <img court> sh` | Run ephemeral interactive sandbox shell |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers (including stopped) |
| `docker stop <container>` | Graceful stop (sends `SIGTERM`, then `SIGKILL`) |
| `docker start <container>` | Start an existing stopped container |
| `docker restart <container>` | Restart a running or stopped container |
| `docker rm -f <container>` | Force-remove a running container |

### 2. Debugging & Introspection
| Command | Description |
| :--- | :--- |
| `docker logs -f <container>` | Stream container stdout / stderr output |
| `docker logs --tail 50 <container>` | View last 50 log lines |
| `docker exec -it <container> sh` | Open interactive shell inside running container |
| `docker inspect <container\|image>` | Low-level JSON metadata, IPs, volume bindings |
| `docker stats` | Live streaming resource usage (CPU%, Memory, Net I/O) |
| `docker top <container>` | Display running processes inside container |

### 3. Images & Build
| Command | Description |
| :--- | :--- |
| `docker build -t <name>:<tag> .` | Build an image from `Dockerfile` in current dir |
| `docker build -f <file> -t <name>:<tag> .` | Build using custom `Dockerfile` path |
| `docker images` | List all local images stored on machine |
| `docker pull <image>:<tag>` | Download image from registry without running |
| `docker push <image>:<tag>` | Upload tagged image to remote registry |
| `docker tag <source> <target>` | Create alias tag pointing to existing image |
| `docker rmi <image>` | Remove local image |
| `docker history <image>` | Show build steps and size per layer |

### 4. Volumes, Networks & Hygiene
| Command | Description |
| :--- | :--- |
| `docker volume ls` | List Docker-managed named volumes |
| `docker volume create <name>` | Create persistent named volume |
| `docker volume inspect <name>` | View host mountpoint path on physical disk |
| `docker network ls` | List bridge, host, and overlay networks |
| `docker system df` | Show disk usage breakdown (images, containers, volumes) |
| `docker system prune` | Remove all stopped containers and unused build caches |
| `docker system prune -a --volumes` | Deep wipe: Remove unused images + unattached volumes |
