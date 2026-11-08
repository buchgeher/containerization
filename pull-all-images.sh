#!/usr/bin/env bash
set -e

echo "============================================================"
echo " Pre-pulling all required container images for FH Labs..."
echo "============================================================"

IMAGES=(
  "hello-world"
  "alpine:latest"
  "alpine:3.19"
  "nginx:alpine"
  "nginxinc/nginx-unprivileged:alpine"
  "python:3.12-alpine"
  "python:3.12-slim"
  "golang:1.22-alpine"
  "golang:1.22"
  "postgres:16-alpine"
)

for img in "${IMAGES[@]}"; do
  echo ""
  echo "==> Pulling $img..."
  docker pull "$img"
done

echo ""
echo "============================================================"
echo "✅ All lab images successfully cached locally!"
echo "You are ready for class without requiring active downloads."
echo "============================================================"
