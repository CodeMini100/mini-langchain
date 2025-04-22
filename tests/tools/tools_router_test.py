import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from main import create_app

# -----------------------------------------------------------------------------
# Test Client Fixture
# -----------------------------------------------------------------------------
@pytest.fixture
def client():
    """
    Provides a TestClient for the FastAPI application created by create_app().
    """
    app = create_app()
    return TestClient(app)


# -----------------------------------------------------------------------------
# call_tool_endpoint Tests
# -----------------------------------------------------------------------------
def test_call_search_tool_success(client):
    """
    Test that calling the /tools/call_tool/search endpoint successfully invokes
    the 'search_tool' from tools_service and returns the expected result.
    """
    # Mock response for the search_tool function
    with patch("tools.tools_service.search_tool") as mock_search_tool:
        mock_search_tool.return_value = {"results": ["mock result"]}

        response = client.post(
            "/tools/call_tool/search",
            json={"tool_input": "test query"}
        )
        assert response.status_code == 200
        assert response.json() == {"results": ["mock result"]}
        mock_search_tool.assert_called_once_with("test query")


def test_call_calculator_tool_success(client):
    """
    Test that calling the /tools/call_tool/calculator endpoint successfully invokes
    the 'calculator_tool' from tools_service and returns the expected result.
    """
    # Mock response for the calculator_tool function
    with patch("tools.tools_service.calculator_tool") as mock_calculator_tool:
        mock_calculator_tool.return_value = {"result": 4}

        response = client.post(
            "/tools/call_tool/calculator",
            json={"tool_input": "2+2"}
        )
        assert response.status_code == 200
        assert response.json() == {"result": 4}
        mock_calculator_tool.assert_called_once_with("2+2")


def test_call_tool_unknown_tool_name(client):
    """
    Test that calling an unrecognized tool name results in an error (e.g., 404 or 400),
    depending on the router's implementation.
    """
    response = client.post("/tools/call_tool/unknown", json={"tool_input": "anything"})
    # Expecting a 404 or 400 depending on the router's handling of invalid tool names
    assert response.status_code in (400, 404)


def test_call_tool_missing_input(client):
    """
    Test that calling the endpoint without providing the required 'tool_input' in JSON
    results in a validation error (422 Unprocessable Entity).
    """
    # Attempt to call the endpoint without the 'tool_input' key
    response = client.post("/tools/call_tool/search", json={})
    assert response.status_code == 422


def test_call_tool_raises_exception(client):
    """
    Test that if the underlying tool function raises an exception, the endpoint
    returns an appropriate error response (500 Internal Server Error by default).
    """
    with patch("tools.tools_service.search_tool", side_effect=Exception("Test error")):
        response = client.post(
            "/tools/call_tool/search",
            json={"tool_input": "trigger error"}
        )
        # Depending on how exceptions are handled, could be 500 or custom status code
        assert response.status_code == 500 or response.status_code == 400  # Adjust as needed