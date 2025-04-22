import pytest
from unittest.mock import MagicMock
from chains.chains_service import build_simple_chain

# -----------------------------------------------------------------------
# Test suite for build_simple_chain function in chains.chains_service.py
# -----------------------------------------------------------------------

@pytest.fixture
def mock_llm_provider():
    """
    Fixture that returns a mocked LLM provider.
    """
    return MagicMock()

def test_build_simple_chain_success(mock_llm_provider):
    """
    Test that build_simple_chain returns a valid chain instance 
    when provided a valid LLM provider.
    """
    chain = build_simple_chain(mock_llm_provider)
    assert chain is not None, "Expected a valid chain instance, got None"
    # Additional assertions can verify the structure or expected fields of the chain
    # Example placeholder, replace with actual checks if needed:
    # assert hasattr(chain, 'prompt'), "Chain should have a 'prompt' attribute"

def test_build_simple_chain_with_none_provider():
    """
    Test that build_simple_chain raises an error when None is passed as the provider.
    """
    with pytest.raises(ValueError):
        build_simple_chain(None)

def test_build_simple_chain_with_invalid_provider():
    """
    Test that build_simple_chain raises an error or handles an invalid provider input gracefully.
    This might depend on custom validation in the function implementation.
    """
    class InvalidProvider:
        pass

    with pytest.raises(TypeError):
        build_simple_chain(InvalidProvider())