from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class ConversationMemoryModel(BaseModel):
    """
    Pydantic model for representing conversation memory.
    """
    id: int = Field(..., description="Unique identifier of the memory.")
    conversation_id: str = Field(..., description="Identifier for the conversation.")
    messages: List[str] = Field(..., description="List of messages in the conversation.")
    created_at: datetime = Field(..., description="Creation timestamp of the memory.")


class ConversationMemory(Base):
    """
    SQLAlchemy model for persisting conversation memory in the database.
    """
    __tablename__ = "conversation_memories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    conversation_id = Column(String, nullable=False, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)

    # TODO: Add relationship or foreign key constraints as needed
    related_data_id = Column(Integer, ForeignKey("related_data.id"), nullable=True)
    related_data = relationship("RelatedDataModel", back_populates="conversation_memories")


class RelatedDataModel(Base):
    """
    Example model for related data. This can be used to store
    additional information linked to a conversation memory.
    """
    __tablename__ = "related_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    extra_info = Column(String, nullable=True)

    # Relationship back to ConversationMemory
    conversation_memories = relationship("ConversationMemory", back_populates="related_data")

    # TODO: Implement any necessary methods or properties for related data
    # Example: error handling or additional validation logic could be placed here if needed.