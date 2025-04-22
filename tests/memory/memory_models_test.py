import pytest
from pydantic import ValidationError
from datetime import datetime

# The skeleton memory_models.py defines "ConversationMemoryModel" with:
# id, conversation_id, messages, created_at

from memory.memory_models import ConversationMemoryModel

@pytest.mark.describe("ConversationMemoryModel Tests")
class TestConversationMemoryModel:
    @pytest.mark.it("Successfully creates a ConversationMemoryModel with valid data")
    def test_conversation_memory_model_valid_data(self):
        instance = ConversationMemoryModel(
            id=1,
            conversation_id="session_123",
            messages=["Hello, AI!"],
            created_at=datetime.utcnow()
        )
        assert instance.id == 1
        assert instance.conversation_id == "session_123"
        assert instance.messages == ["Hello, AI!"]
        assert isinstance(instance.created_at, datetime)

    @pytest.mark.it("Fails to create a ConversationMemoryModel when a required field is missing")
    def test_conversation_memory_model_missing_required_field(self):
        with pytest.raises(ValidationError):
            # Missing 'id' field
            ConversationMemoryModel(
                conversation_id="session_123",
                messages=["Hello, AI!"],
                created_at=datetime.utcnow()
            )

    @pytest.mark.it("Fails to create a ConversationMemoryModel with invalid data types")
    def test_conversation_memory_model_invalid_types(self):
        with pytest.raises(ValidationError):
            ConversationMemoryModel(
                id="string_instead_of_int",
                conversation_id=123,          # expecting a str
                messages="Not a list",        # expecting a list
                created_at="invalid_datetime" # expecting datetime
            )