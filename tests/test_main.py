"""Test the endpoints specified in main.py."""

from fastapi.testclient import TestClient

from my_fastapi_app.main import app

client: TestClient = TestClient(app=app)


def test_root():
    """Test the '/' endpoint of the FastAPI app."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}
