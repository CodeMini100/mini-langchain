import pytest
from unittest.mock import MagicMock, patch
from agents.agents_service import create_basic_agent, run_agent_query

"""
Tests for agents.agents_service.py

Functions under test:
1. create_basic_agent(tools) - Builds an agent that can utilize a provided set of tools
2. run_agent_query(agent, user_query) - Passes a query to the agent, handles the chain of thought

We will verify:
- The agent is created correctly with valid and invalid tool inputs.
- run_agent_query returns expected output given a mock agent.
- Proper error handling when invalid arguments are provided.
"""

@pytest.fixture
def mock_tools():
    """
    Returns a list of mocked tools. Each tool can be a callable or
    some representation that the agent expects to use.
    """
    tool_1 = MagicMock(name="search_tool")
    tool_2 = MagicMock(name="calculator_tool")
    return [tool_1, tool_2]

@pytest.fixture
def mock_agent(mock_tools):
    """
    Creates a basic agent (using create_basic_agent) with the mock tools.
    This fixture can be used for testing run_agent_query.
    """
    return create_basic_agent(mock_tools)

def test_create_basic_agent_with_valid_tools(mock_tools):
    """
    Test that create_basic_agent returns a valid agent object
    when provided with a list of tools.
    """
    agent = create_basic_agent(mock_tools)
    assert agent is not None, "Agent should not be None"
    # Here we assume the returned agent might store or reference the tools internally
    # We can further assert certain attributes if known, otherwise just check existence
    assert hasattr(agent, "tools") or hasattr(agent, "toolkit"), "Agent should have a reference to the tools"

def test_create_basic_agent_with_empty_tools():
    """
    Test that create_basic_agent handles an empty list of tools gracefully.
    """
    empty_tools = []
    agent = create_basic_agent(empty_tools)
    assert agent is not None, "Agent should still be created even with no tools"
    # If needed, we can assert that the agent has zero tools
    # But here we check it does not crash or raise an error

def test_run_agent_query_with_valid_agent_and_query(mock_agent):
    """
    Test that run_agent_query returns an expected response when provided
    with a valid agent and a non-empty user query.
    We'll mock the agent's internal behavior to return a known result.
    """
    # Patch the agent's internal run function if it exists. This depends on implementation details.
    with patch.object(mock_agent, 'run', return_value="Mocked agent response") as mock_run:
        response = run_agent_query(mock_agent, "Hello, agent!")
        mock_run.assert_called_once_with("Hello, agent!")
        assert response == "Mocked agent response", "run_agent_query should return the agent's response"

def test_run_agent_query_with_none_agent():
    """
    Test that run_agent_query handles a None agent by raising an error or returning an error message.
    """
    with pytest.raises(ValueError, match="Agent cannot be None"):
        run_agent_query(None, "User query")

def test_run_agent_query_with_empty_query(mock_agent):
    """
    Test that run_agent_query handles an empty user query. Depending on implementation,
    it might raise an error or return a default response.
    """
    with pytest.raises(ValueError, match="User query cannot be empty"):
        run_agent_query(mock_agent, "")