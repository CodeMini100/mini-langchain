import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# Import the functions under test using absolute imports from the project root
from main import create_app, run_app


@pytest.fixture
def test_client():
    """
    Pytest fixture to create a TestClient instance of the FastAPI app.
    Ensures setup and teardown around each test if needed.
    """
    app = create_app()
    return TestClient(app)


def test_create_app_returns_fastapi_instance(test_client):
    """
    Test that create_app successfully returns a FastAPI application
    by checking a known, automatically generated route: /docs
    """
    response = test_client.get("/docs")
    assert response.status_code == 200, "Expected /docs to return 200 OK"


def test_run_app_starts_server():
    """
    Test the run_app function to ensure it attempts to
    start the server using uvicorn.
    This is done by mocking uvicorn.run and verifying the call.
    """
    with patch("uvicorn.run") as mock_run:
        run_app()
        mock_run.assert_called_once()
        # Optionally, we could check args/kwargs if the function passes specific parameters to uvicorn:
        # mock_run.assert_called_once_with("main:create_app", host="0.0.0.0", port=8000, reload=True)