# Use modern, lightweight official Python slim image
FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Step 1: Install dependencies (leveraging Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 2: Copy application source code
COPY main.py .

# Step 3: Run as unprivileged non-root user (security best practice)
USER nobody

EXPOSE 8000

# Step 4: Production ASGI server invocation
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

