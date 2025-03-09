from abc import ABC, abstractmethod

class ChainInterface(ABC):
    @abstractmethod
    def run(self, input_data: dict) -> dict:
        """
        Execute the chain of processing steps.
        TODO: Validate input_data, log entry/exit, and update context.
        Hint: Use try/except blocks, for example:
            try:
                # process input
            except Exception as e:
                # log error and handle
        """
        pass

    @abstractmethod
    def add_step(self, step):
        """
        Add a processing step to the chain.
        TODO: Check that 'step' is callable and logs its addition.
        Hint: You might check:
            if not callable(step):
                raise ValueError("Step must be callable")
        """
        pass