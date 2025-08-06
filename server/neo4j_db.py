import os
from neo4j import AsyncGraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URL = os.getenv("NEO4J_URL", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Neo4j setup
neo4j_driver = AsyncGraphDatabase.driver(
    NEO4J_URL,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

async def get_neo4j():
    async with neo4j_driver.session() as session:
        try:
            yield session
        finally:
            await session.close()

async def close_neo4j():
    await neo4j_driver.close()