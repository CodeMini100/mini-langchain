import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

# Import the FastAPI app factory
from main import create_app

"""
Tests for memory_router.py

Functions tested:
1. get_memory_state_endpoint(session_id) - Returns the memory content for a given session
2. clear_memory_endpoint(session_id) - Clears memory for a given session
"""

@pytest.fixture
def client():
    """
    Fixture to create a TestClient instance for FastAPI app.
    """
    app = create_app()
    return TestClient(app)

@patch("memory.memory_router.retrieve_memory")
def test_get_memory_state_endpoint_success(mock_retrieve_memory, client):
    """
    Test if get_memory_state_endpoint successfully returns
    the conversation history for an existing session.
    """
    session_id = "test-session"
    mock_retrieve_memory.return_value = ["User: Hello", "AI: Hi there!"]

    response = client.get(f"/memory/{session_id}")

    assert response.status_code == 200
    assert response.json() == ["User: Hello", "AI: Hi there!"]
    mock_retrieve_memory.assert_called_once_with(session_id)

@patch("memory.memory_router.retrieve_memory")
def test_get_memory_state_endpoint_no_session(mock_retrieve_memory, client):
    """
    Test if get_memory_state_endpoint handles a session with no stored memory
    by returning an empty array or appropriate response.
    """
    session_id = "nonexistent-session"
    mock_retrieve_memory.return_value = []

    response = client.get(f"/memory/{session_id}")

    assert response.status_code == 200
    assert response.json() == []
    mock_retrieve_memory.assert_called_once_with(session_id)

@patch("memory.memory_router.retrieve_memory")
def test_clear_memory_endpoint_success(mock_retrieve_memory, client):
    """
    Test if clear_memory_endpoint clears the memory for a valid session correctly.
    Verifies that subsequent retrieval returns empty memory.
    """
    session_id = "test-session"

    # Clear the memory for the session
    delete_response = client.delete(f"/memory/{session_id}")
    assert delete_response.status_code == 200

    # Mock retrieve_memory to return an empty list after clearing
    mock_retrieve_memory.return_value = []
    get_response = client.get(f"/memory/{session_id}")
    assert get_response.status_code == 200
    assert get_response.json() == []

def test_clear_memory_endpoint_no_session(client):
    """
    Test if clear_memory_endpoint gracefully handles
    clearing memory for a session that doesn't exist.
    """
    session_id = "nonexistent-session"
    response = client.delete(f"/memory/{session_id}")

    # Depending on how the endpoint is implemented, it might return 200 or 404.
    assert response.status_code in [200, 404]