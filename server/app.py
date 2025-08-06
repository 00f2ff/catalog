from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from postgres_db import get_db
from neo4j_db import get_neo4j
from schemas import HealthResponse, ServiceStatus

app = FastAPI(title="Catalog API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello from Catalog API!"}

@app.get("/health", response_model=HealthResponse)
async def health_check(
    db: AsyncSession = Depends(get_db),
    neo4j_session = Depends(get_neo4j)
) -> HealthResponse:
    services = {}
    overall_status = "healthy"
    
    # Check PostgreSQL
    try:
        await db.execute("SELECT 1")
        services["postgres"] = "connected"
    except Exception as e:
        overall_status = "unhealthy"
        services["postgres"] = ServiceStatus(status="disconnected", error=str(e))
    
    # Check Neo4j
    try:
        result = await neo4j_session.run("RETURN 1 AS test")
        await result.single()
        services["neo4j"] = "connected"
    except Exception as e:
        overall_status = "unhealthy"
        services["neo4j"] = ServiceStatus(status="disconnected", error=str(e))
    
    return HealthResponse(status=overall_status, services=services)

@app.get("/items")
async def get_items(db: AsyncSession = Depends(get_db)):
    # Example endpoint showing session usage
    return {"items": [], "message": "Database session available"}