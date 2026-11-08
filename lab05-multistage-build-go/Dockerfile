# ==========================================
# Stage 1: Build the static Go binary
# ==========================================
FROM golang:1.22-alpine AS builder

WORKDIR /build

# Copy source code
COPY main.go .

# CGO_ENABLED=0 produces a statically linked binary (no libc dependency)
# GOOS=linux targets the container Linux OS
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o server .

# ==========================================
# Stage 2: Minimal production runtime
# ==========================================
FROM alpine:3.19

WORKDIR /app

# Copy ONLY the compiled binary from the builder stage!
COPY --from=builder /build/server .

# Non-root user
USER nobody

EXPOSE 8090

ENTRYPOINT ["./server"]
