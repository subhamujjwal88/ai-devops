import os
from fastapi import FastAPI

app = FastAPI(
    title="DevOps Practice App",
    description="A simple API for learning DevOps step-by-step",
    version="1.0.0",
)

APP_ENV = os.getenv("APP_ENV", "development")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.get("/")
def read_root():
    """Root endpoint providing a welcoming message."""
    return {
        "message": "Welcome to the DevOps Practice App!",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    """Health check endpoint used to verify the app is running."""
    return {"status": "healthy"}


@app.get("/info")
def app_info():
    """Application metadata endpoint showing version and environment."""
    return {
        "app": "DevOps Practice App",
        "version": APP_VERSION,
        "environment": APP_ENV,
    }
