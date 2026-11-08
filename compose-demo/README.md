# Docker Compose Multi-Container Demo

Demonstrates how to declare and orchestrate a multi-container stack (Nginx web tier + PostgreSQL database tier) on a single Docker host with isolated networking and persistent storage.

---

## Step 1: Start the Entire Stack

From this directory (`compose-demo/`), execute:

```bash
docker compose up -d
```

Docker Compose automatically:
1. Creates an isolated bridge network (`compose-demo_app-net`).
2. Creates the persistent named volume (`compose-demo_db-data`).
3. Starts the PostgreSQL container and provisions the database.
4. Starts the web container with a live bind mount to `./html`.

---

## Step 2: Test & Inspect

- Visit `http://localhost:8080` in your web browser.
- Check running status:
  ```bash
  docker compose ps
  ```
- View combined multi-container logs:
  ```bash
  docker compose logs -f
  ```

---

## Step 3: Teardown

```bash
# Stop containers and preserve database volume:
docker compose down

# Or stop and completely wipe persistent volumes (clean slate):
docker compose down -v
```
