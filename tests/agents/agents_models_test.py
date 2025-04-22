import pytest
from pydantic import ValidationError

# Rename these imports to match skeleton agents_models.py
from agents.agents_models import AgentInput, AgentOutput

@pytest.fixture
def valid_query_data():
    """
    Provides valid data for initializing AgentInput.
    """
    return {
        "user_query": "What is the capital of France?"
    }

@pytest.fixture
def invalid_query_data():
    """
    Provides invalid data (missing required fields) for initializing AgentInput.
    """
    return {
        # "user_query" is intentionally omitted to trigger validation error
    }

@pytest.fixture
def valid_response_data():
    """
    Provides valid data for initializing AgentOutput.
    """
    return {
        "final_answer": "The capital of France is Paris.",
        "chain_of_thought": "Step 1: Identify question; Step 2: Provide answer"
    }

@pytest.fixture
def invalid_response_data():
    """
    Provides invalid data for initializing AgentOutput (type mismatch).
    """
    return {
        "final_answer": 1234,  # final_answer should be a string
        "chain_of_thought": 42  # should be a string or None
    }

def test_agent_input_model_valid_input(valid_query_data):
    """
    Test that AgentInput correctly validates and initializes with valid input.
    """
    model_instance = AgentInput(**valid_query_data)
    assert model_instance.user_query == valid_query_data["user_query"]

def test_agent_input_model_invalid_input(invalid_query_data):
    """
    Test that AgentInput raises a ValidationError when required fields are missing or invalid.
    """
    with pytest.raises(ValidationError):
        AgentInput(**invalid_query_data)

def test_agent_output_model_valid_input(valid_response_data):
    """
    Test that AgentOutput correctly validates and initializes with valid input.
    """
    model_instance = AgentOutput(**valid_response_data)
    assert model_instance.final_answer == valid_response_data["final_answer"]
    assert model_instance.chain_of_thought == valid_response_data["chain_of_thought"]

def test_agent_output_model_invalid_input(invalid_response_data):
    """
    Test that AgentOutput raises a ValidationError on type mismatches or missing fields.
    """
    with pytest.raises(ValidationError):
        AgentOutput(**invalid_response_data)