import pytest
from unittest.mock import patch
from memory.memory_service import MemoryService

@pytest.fixture
def memory_service_mock():
    """
    Fixture that patches the in-memory store in MemoryService to ensure a clean slate for each test.
    """
    with patch.object(MemoryService, '_sessions', {}):
        yield

def test_store_message_success(memory_service_mock):
    """
    Test that store_message() successfully stores a user message in memory.
    """
    session_id = "test_session"
    message = "Hello, this is a user message."

    svc = MemoryService()
    svc.store_message(session_id, message)
    history = svc.retrieve_memory(session_id)

    assert len(history) == 1, "Expected one message in the conversation history"
    assert history[0] == message, "Stored message should match the input message"

def test_store_message_multiple_calls(memory_service_mock):
    """
    Test that multiple messages for the same session are stored in order.
    """
    session_id = "test_session"
    messages = ["User message 1", "AI response", "User message 2"]

    svc = MemoryService()
    for msg in messages:
        svc.store_message(session_id, msg)

    history = svc.retrieve_memory(session_id)

    assert len(history) == len(messages), "Expected all messages to be stored"
    assert history == messages, "Messages should match the order they were inserted"

def test_store_message_different_sessions(memory_service_mock):
    """
    Sessions must maintain separate conversation histories.
    """
    svc = MemoryService()

    session_id_1 = "test_session_1"
    session_id_2 = "test_session_2"

    svc.store_message(session_id_1, "Message for session 1")
    svc.store_message(session_id_2, "Message for session 2")

    history_1 = svc.retrieve_memory(session_id_1)
    history_2 = svc.retrieve_memory(session_id_2)

    assert len(history_1) == 1 and history_1[0] == "Message for session 1"
    assert len(history_2) == 1 and history_2[0] == "Message for session 2"

def test_retrieve_memory_empty_session(memory_service_mock):
    """
    Retrieving an empty session should return an empty list.
    """
    svc = MemoryService()
    session_id = "non_existent_session"

    history = svc.retrieve_memory(session_id)
    assert history == [], "Expected empty history for a non-existent session"

def test_store_message_none_session_id(memory_service_mock):
    """
    Storing a message with None session_id should raise ValueError.
    """
    svc = MemoryService()
    with pytest.raises(ValueError):
        svc.store_message(None, "Some message")

def test_store_message_none_message(memory_service_mock):
    """
    Storing a None message should raise ValueError.
    """
    svc = MemoryService()
    with pytest.raises(ValueError):
        svc.store_message("test_session", None)