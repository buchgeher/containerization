# Lab 5: Multi-Stage Builds (Go Microservice)

Learn how multi-stage builds enable **reproducible, hermetic builds** without requiring compilers (Go, Rust, C++) installed on your developer laptop, while slashing production image size from hundreds of megabytes to mere megabytes.

---

## Step 1: Build the Multi-Stage Image

Notice: You do **not** need the Go SDK installed locally. Docker downloads the official builder, compiles the binary hermetically inside the container, and discards all build tools for the final stage.

```bash
docker build -t go-microservice:v1.0 .
```

---

## Step 2: Run & Test the Microservice

```bash
docker run -d --name go-app -p 8090:8090 go-microservice:v1.0

# Smoke test
curl http://localhost:8090
curl http://localhost:8090/health
```

---

## Step 3: Inspect & Compare Image Sizes

Check the size of your compiled image:

```bash
docker images go-microservice:v1.0
```

> **Size:** ~12–15 MB!  
> Compare this with `golang:1.22` which weighs in at **~850 MB**!  
> You achieved a **>98% reduction** in image footprint, eliminating hundreds of unused packages and attack vectors from production.

---

## Cleanup

```bash
docker stop go-app && docker rm go-app
```

