# Lab 4: Building a Custom Container & Security Hardening

Build a custom Docker image, perform security introspection, and refactor the image to drop root privileges.

---

## Step 1: Build the Initial (Naive) Container Image

```bash
docker build -f Dockerfile.v1-root -t raas-web:v1.0 .
```

---

## Step 2: Run & Perform Security Introspection

```bash
# Run container instance
docker run -d --name raas-app -p 8085:80 raas-web:v1.0

# Smoke test
curl http://localhost:8085

# Security Check: Who runs the process inside the container?
docker exec raas-app whoami
# -> Output: root ⚠️

docker exec raas-app id
# -> Output: uid=0(root) gid=0(root)
```

> **Why is this a security hazard?**  
> Containers share the host Linux kernel. If an attacker discovers a Remote Code Execution (RCE) vulnerability and triggers a *container breakout*, they immediately possess **root privileges on your host machine**!

---

## Step 3: Hardening & Refactoring to Non-Root

Inspect `Dockerfile` (which uses `nginxinc/nginx-unprivileged:alpine`):

```bash
# Clean up root container
docker stop raas-app && docker rm raas-app

# Build hardened version
docker build -t raas-web:v2.0 .

# Run hardened container on non-root port 8080
docker run -d --name raas-app-secure -p 8085:8080 raas-web:v2.0

# Verify identity
docker exec raas-app-secure whoami
# -> Output: nginx ✅

docker exec raas-app-secure id
# -> Output: uid=101(nginx) gid=101(nginx)
```

---

## Cleanup

```bash
docker stop raas-app-secure && docker rm raas-app-secure
```

