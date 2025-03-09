from libs.core.langchain_core.llm_interface import LLMInterface
import time
import random

class DummyLLM(LLMInterface):
    def __init__(self):
        """
        Initialize the dummy LLM.
        TODO: Set up simulation parameters such as delay and error probability.
        Hint: self.delay = 0.5, self.error_rate = 0.1
        """
        pass

    def generate(self, prompt: str) -> str:
        """
        Simulate generating a response.
        TODO:
          - Log the received prompt.
          - Optionally sleep for self.delay seconds.
          - Randomly simulate an error based on error_rate.
          - Return a formatted simulated response.
        Hint:
            if random.random() < self.error_rate:
                raise Exception("Simulated LLM error")
            return f"Simulated response to: {prompt}"
        """
        pass
