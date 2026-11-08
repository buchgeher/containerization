# Lab 1: Docker Commands & Local Environment

In this lab, you verify your Docker installation, inspect the client/daemon separation, run lightweight containers, and inspect process namespaces.

---

## Step 1: Verify Engine & System Info

```bash
# Check client and server daemon version
docker version

# Detailed system summary (storage driver, CPU/RAM limits, runtimes)
docker info
```

---

## Step 2: Hello World & Execution Flags

```bash
# Pull and run the canonical verification image
docker run hello-world

# Run an ephemeral container that cleans up after exit (--rm)
docker run --rm alpine echo "Hello from isolated Alpine container!"
```

---

## Step 3: Container Inspection & Namespaces

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
