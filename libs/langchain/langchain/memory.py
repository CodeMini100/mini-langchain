from libs.core.langchain_core.memory_interface import MemoryInterface

class InMemoryMemory(MemoryInterface):
    def __init__(self):
        """
        Initialize in-memory storage.
        TODO: Create an empty dictionary for storage.
        Hint: self._store = {}
        """
        pass

    def load(self) -> dict:
        """
        Load and return current context.
        TODO: Return the stored context with logging.
        Hint: return self._store.copy()
        """
        pass

    def save(self, context: dict):
        """
        Save or update the memory with new data.
        TODO:
          - Validate input.
          - Merge new context into self._store.
          - Log the update.
        Hint: Use self._store.update(context)
        """
        pass
