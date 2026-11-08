# Lab 2: Port Mapping, Bind Mounts & Container Shell

Learn how to expose network ports, mount a local host directory into a running container for instant live-reloading, and attach an interactive shell.

---

## Step 1: Start Container with a Bind Mount

From this directory (`lab02-bind-mount-live-reload/`), run:

```bash
docker run -d --name my-webserver \
  -p 8080:80 \
  -v $(pwd)/index.html:/usr/share/nginx/html/index.html:ro \
  nginx:alpine
```

- `-p 8080:80`: Maps localhost port 8080 to container port 80.
- `-v $(pwd)/index.html:...:ro`: Mounts host file read-only into Nginx document root.

### Test:
Open `http://localhost:8080` in your browser or execute:

```bash
curl http://localhost:8080
```

---

## Step 2: Live-Reload without Rebuilding Image!

Edit `index.html` on your host machine (change the title or colors).  
Then refresh your browser or re-run `curl http://localhost:8080`.

Notice that the update is **instantaneous** — no container rebuild, restart, or file copy required!

---

## Step 3: Interactive Shell inside Container (`exec`)

Attach an interactive terminal directly into the container's namespaces:

```bash
# Attach shell
docker exec -it my-webserver sh

# Inspect container environment
/ # ls -la /usr/share/nginx/html
/ # cat /usr/share/nginx/html/index.html
/ # ps aux
/ # exit
```

---

## Step 4: Cleanup

```bash
# Stream logs
docker logs my-webserver

# Stop and remove
docker stop my-webserver && docker rm my-webserver
```
