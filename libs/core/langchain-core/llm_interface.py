from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a text response based on the given prompt.
        TODO: Include error handling and logging.
        Hint: You may simulate a delay or check for empty prompt.
        """
        pass
