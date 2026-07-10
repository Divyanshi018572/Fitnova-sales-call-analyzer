"""
Main entrypoint for the FitNova FastAPI application.

Why this approach:
This module initializes the FastAPI application, mounts CORS/security settings if needed,
and registers all sub-routers (calls, summaries, contests) to expose the core business
and feedback capabilities to the frontend dashboard.
"""

from fastapi import FastAPI
from src.storage.db import engine, Base
from src.storage import models  # Ensure SQLAlchemy models are registered
from src.api.routers import calls, summaries, contests

# Create all database tables on start (safe/idempotent)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FitNova Sales-Call Intelligence API",
    description="Automated analysis, compliance scoring, and ingestion pipeline for FitNova sales calls.",
    version="1.0.0"
)

# Register routers
app.include_router(calls.router)
app.include_router(summaries.router)
app.include_router(contests.router)

@app.get("/")
def read_root():
    """
    Root endpoint for service identification.
    """
    return {"status": "ok", "service": "FitNova Call Intelligence API"}

@app.get("/health")
def health_check():
    """
    Health check endpoint for Docker container and Render deployment monitoring.
    """
    return {"status": "healthy"}
