from pydantic import BaseModel

class ServiceStatus(BaseModel):
    status: str
    error: str | None = None

class HealthResponse(BaseModel):
    status: str
    services: dict[str, str | ServiceStatus]