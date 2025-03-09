from libs.core.langchain_core.chain_interface import ChainInterface

class ChainExecutor(ChainInterface):
    def __init__(self):
        # TODO: Initialize your chain executor with an empty steps list and context.
        # Hint: self.steps = [] and self.context = {}
        pass

    def add_step(self, step):
        """
        Add a processing step to the chain.
        TODO: Validate that step is callable and log its addition.
        Hint: if not callable(step): raise ValueError("Step must be callable")
        """
        pass

    def run(self, input_data: dict) -> dict:
        """
        Execute the chain sequentially.
        TODO:
          - Merge input_data into the current context.
          - Iterate through each step: log start, execute, validate output, update context.
          - Use try/except to catch errors and decide on recovery.
        Hint: For each step, check if isinstance(result, dict) before merging.
        """
        pass
