import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from main import create_app


@pytest.fixture
def client():
    """
    Fixture to create a TestClient instance for the FastAPI app.
    """
    app = create_app()
    return TestClient(app)


def test_generate_text_endpoint_success(client, mocker):
    """
    Test successful text generation with valid input.
    Mocks the chain so we don't rely on external LLM calls.
    """
    # Arrange
    mock_chain_output = "Mocked chain output"
    mock_chain = MagicMock()
    mock_chain.run.return_value = mock_chain_output

    # Mock the build_simple_chain function to return our mock chain
    mock_build_chain = mocker.patch(
        "chains.chains_service.build_simple_chain",
        return_value=mock_chain
    )

    request_data = {"input_text": "Hello from test"}

    # Act
    response = client.post("/chains/generate_text_endpoint", json=request_data)

    # Assert
    assert response.status_code == 200
    json_response = response.json()
    assert "generated_text" in json_response
    assert json_response["generated_text"] == mock_chain_output

    # Verify our chain functions were called as expected
    mock_build_chain.assert_called_once()
    mock_chain.run.assert_called_once_with(request_data["input_text"])


def test_generate_text_endpoint_missing_input(client):
    """
    Test that the endpoint handles missing or invalid request data appropriately.
    Expecting a 422 (Unprocessable Entity) or 400 (Bad Request) response.
    """
    # Act
    response = client.post("/chains/generate_text_endpoint", json={})

    # Assert
    # Adjust your status code expectations based on how your app handles invalid input
    assert response.status_code in [400, 422], (
        f"Expected 400 or 422, got {response.status_code}"
    )


def test_generate_text_endpoint_error_handling(client, mocker):
    """
    Test that the endpoint correctly handles errors thrown by the chain.
    """
    # Arrange
    mock_chain = MagicMock()
    mock_chain.run.side_effect = Exception("Chain error")

    mocker.patch(
        "chains.chains_service.build_simple_chain",
        return_value=mock_chain
    )

    request_data = {"input_text": "This will trigger an error"}

    # Act
    response = client.post("/chains/generate_text_endpoint", json=request_data)

    # Assert
    # Adjust your status code and response structure based on your error handling
    assert response.status_code == 500
    json_response = response.json()
    assert "detail" in json_response
    assert json_response["detail"] == "Chain error"