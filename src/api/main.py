"""
Main entrypoint for the FitNova FastAPI application.

Why this approach:
This module initializes the FastAPI application and defines basic health check routes. 
Using FastAPI allows for asynchronous, auto-documented endpoints which serve as the
integration layer between the database, the analysis pipeline, and the dashboard frontend.
"""

from fastapi import FastAPI

app = FastAPI(
    title="FitNova Sales-Call Intelligence API",
    description="Automated analysis, scoring, and ingestion pipeline for FitNova sales calls.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    """
    Root endpoint for service identification.
    
    Returns basic service status and name.
    """
    return {"status": "ok", "service": "FitNova Call Intelligence API"}

@app.get("/health")
def health_check():
    """
    Health check endpoint for container and deployment monitoring.
    """
    return {"status": "healthy"}
