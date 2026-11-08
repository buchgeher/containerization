from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import datetime
import os

app = FastAPI(
    title="Fleet Telemetry Service",
    description="Python FastAPI Microservice Starter for Robotics & IoT",
    version="1.0.0",
)

class TelemetryPayload(BaseModel):
    robot_id: str
    battery_level: float
    status: str
    speed_mps: Optional[float] = 0.0

@app.get("/")
def read_root():
    return {
        "service": "Fleet Telemetry Service",
        "status": "online",
        "docs_url": "/docs",
        "container_time": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "pod_host": os.getenv("HOSTNAME", "local-docker"),
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "telemetry-api"}

@app.post("/api/v1/telemetry")
def record_telemetry(payload: TelemetryPayload):
    return {
        "message": "Telemetry received successfully",
        "robot_id": payload.robot_id,
        "battery_level": payload.battery_level,
        "status": payload.status,
        "recorded_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

