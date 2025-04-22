import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from main import create_app
from agents.agents_service import run_agent_query

# --------------------------------------------------------------------------------
# FIXTURES
# --------------------------------------------------------------------------------

@pytest.fixture
def client():
    """
    Fixture to create a TestClient instance for FastAPI app.
    """
    app = create_app()
    return TestClient(app)

# --------------------------------------------------------------------------------
# TESTS
# --------------------------------------------------------------------------------

@pytest.mark.describe("Agents Router - agent_query_endpoint Tests")
class TestAgentQueryEndpoint:
    @pytest.mark.it("should return a successful response with the agent's final answer")
    @patch("agents.agents_service.run_agent_query")
    def test_agent_query_success(self, mock_run_agent_query, client):
        """
        Test that a valid agent query returns the final answer from the agent.
        """
        # Arrange
        # Mock the service function to simulate successful agent processing
        mock_run_agent_query.return_value = "Mocked final answer"

        # Example request payload
        request_data = {
            "user_query": "Hello, how are you?"
        }

        # Act
        response = client.post("/agents/agent_query", json=request_data)

        # Assert
        assert response.status_code == 200
        json_response = response.json()
        assert "answer" in json_response
        assert json_response["answer"] == "Mocked final answer"
        mock_run_agent_query.assert_called_once()

    @pytest.mark.it("should return 422 when the request body is missing required fields")
    def test_agent_query_missing_fields(self, client):
        """
        Test that an unprocessable entity (422) is returned if required fields are missing.
        """
        # Arrange
        # Missing 'user_query' in request_data
        request_data = {}

        # Act
        response = client.post("/agents/agent_query", json=request_data)

        # Assert
        # FastAPI will typically respond with a 422 status code for validation errors
        assert response.status_code == 422

    @pytest.mark.it("should return 500 when an internal error occurs in the agent query service")
    @patch("agents.agents_service.run_agent_query")
    def test_agent_query_internal_error(self, mock_run_agent_query, client):
        """
        Test that a 500 status code is returned if the internal service function raises an error.
        """
        # Arrange
        # Simulate an internal exception
        mock_run_agent_query.side_effect = Exception("Internal service error")

        request_data = {
            "user_query": "Trigger error"
        }

        # Act
        response = client.post("/agents/agent_query", json=request_data)

        # Assert
        # Expect a 500 status code or some error response
        # The actual status code may vary depending on error handling in the router
        # Adjust accordingly if the code handles exceptions differently (e.g., returning 400 or 404)
        assert response.status_code == 500

        json_response = response.json()
        assert "detail" in json_response
        assert "Internal service error" in json_response["detail"]