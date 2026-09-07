from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """Test that the root endpoint returns 200 OK and expected greeting."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Welcome to the AI DevOps Practice App!"


def test_health_check():
    """Test that the health endpoint returns 200 OK and healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data == {"status": "healthy"}


def test_app_info():
    """Test that the info endpoint returns 200 OK and app metadata."""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "DevOps Practice App"
    assert "version" in data
    assert "environment" in data
