# Lab 3: Persistent Data with Named Volume Mounts

Demonstrates why containers are ephemeral by default, how to create Docker-managed Named Volumes, and how data persists across container deletion.

---

## Step 1: Create a Managed Docker Volume

```bash
# Create volume
docker volume create guestbook-data

# Inspect Docker daemon storage path
docker volume inspect guestbook-data
```

---

## Step 2: Run Guestbook App with Volume Mount

From this directory (`lab03-volume-persistence-guestbook/`), run:

```bash
docker run -d --name guestbook-app \
  -p 8000:8000 \
  -v guestbook-data:/data \
  -v $(pwd)/app.py:/app/app.py:ro \
  -w /app \
  python:3.12-alpine \
  python app.py
```

### Explanation of flags:
- `-v guestbook-data:/data`: Mounts our managed volume to `/data` inside the container.
- `-v $(pwd)/app.py:/app/app.py:ro`: Mounts the single Python script read-only.
- `-w /app`: Sets working directory.
- `python:3.12-alpine python app.py`: Executes standard official Python without writing a custom image.

---

## Step 3: Add Data via Browser

1. Open `http://localhost:8000` in your web browser.
2. Enter 2–3 messages into the input field and click **Submit Entry**.
3. Notice how they appear in the *Saved Messages* list.

---

## Step 4: Verify the Written File Inside the Volume

```bash
docker exec guestbook-app cat /data/entries.txt
```

You will see timestamps and the exact text lines written by the web app!

---

## Step 5: The Test — Destroy the Container

Forcefully terminate and delete the container:

```bash
docker rm -f guestbook-app
```

Verify that the container is completely gone:

```bash
docker ps -a
```

---

## Step 6: Start a Brand New Container & Verify Persistence

Spin up a completely fresh container instance attached to the same volume:

```bash
docker run -d --name guestbook-app2 \
  -p 8000:8000 \
  -v guestbook-data:/data \
  -v $(pwd)/app.py:/app/app.py:ro \
  -w /app \
  python:3.12-alpine \
  python app.py
```

Now reload `http://localhost:8000` in your browser.

🎉 **Outcome:** All your previously submitted entries are fully intact! The container lifecycle is completely decoupled from your stateful data.

---

## Cleanup

```bash
# Stop and delete container
docker rm -f guestbook-app2

# Remove the volume (when done with testing)
docker volume rm guestbook-data
```
