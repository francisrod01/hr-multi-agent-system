"""FastAPI entry point."""

from fastapi import FastAPI
from src.core.settings import settings
from src.utils.logging_conf import configure_logging

# Configure logging
configure_logging()

app = FastAPI(title="HR Multi-Agent System", version="0.1.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "environment": settings.environment}

@app.get("/")
async def root():
    return {"message": "HR Multi-Agent System API", "status": "running"}
