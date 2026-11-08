# Production Hardened Dockerfile
# 1. Unprivileged base image (pre-configured with user 'nginx' and port 8080)
FROM nginxinc/nginx-unprivileged:alpine

# 2. Copy static assets
COPY index.html /usr/share/nginx/html/index.html

# 3. Expose unprivileged port (>= 1024)
EXPOSE 8080

# 4. Explicitly drop all root privileges
USER nginx

