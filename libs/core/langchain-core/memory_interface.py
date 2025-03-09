from abc import ABC, abstractmethod

class MemoryInterface(ABC):
    @abstractmethod
    def load(self) -> dict:
        """
        Load and return the stored context.
        TODO: Add logging and error checking.
        Hint: Consider returning a copy of the memory dictionary.
        """
        pass

    @abstractmethod
    def save(self, context: dict):
        """
        Save or update the memory with new context.
        TODO: Validate and merge context, log the update.
        Hint: Use dict.update() after validation.
        """
        pass
