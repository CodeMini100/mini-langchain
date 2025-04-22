from typing import Dict, List


class MemoryService:
    """
    Provides memory storage and retrieval for chat sessions.
    Can be adapted to use in-memory, database, or external storage mechanisms.
    """

    def __init__(self) -> None:
        """
        Initializes the MemoryService with an in-memory data structure.

        TODO: Replace with DB or external store implementation if needed.
        """
        self._sessions: Dict[str, List[str]] = {}

    def store_message(self, session_id: str, message: str) -> None:
        """
        Persists a user or AI message in memory for a specific session.
        
        :param session_id: Unique identifier for the chat session.
        :param message: The message to be stored.
        :raises ValueError: If session_id or message is empty.
        """
        if not session_id:
            raise ValueError("Session ID cannot be empty.")
        if not message:
            raise ValueError("Message cannot be empty.")

        if session_id not in self._sessions:
            self._sessions[session_id] = []

        self._sessions[session_id].append(message)

    def retrieve_memory(self, session_id: str) -> List[str]:
        """
        Retrieves the full conversation history for a specific session.
        
        :param session_id: Unique identifier for the chat session.
        :return: A list of messages corresponding to the session.
        :raises ValueError: If session_id is empty.
        """
        if not session_id:
            raise ValueError("Session ID cannot be empty.")

        return self._sessions.get(session_id, [])