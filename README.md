Project Editorial – Build langchain lite
====================================================================================

Overview:
---------
This project will help you build your own version of the langchain framework. 

It provides a modular framework that incorporates:
  - Graph-based execution (DAG) for managing complex workflows.
  - Dynamic state management with checkpointing and rollback.
  - Agentic decision-making to choose execution paths.
  - Integration of external tools via a standardized interface.
  - A command-line interface (CLI) for interactive use.
  - Comprehensive logging, testing, and documentation.

---------------------------------------------------------------------
Task Breakdown & Detailed Hints:
---------------------------------------------------------------------

Task 1: Core Abstractions
-------------------------
Objective:
  - Define abstract interfaces that serve as the foundation for all modules.
  - Interfaces include:
      * ChainInterface: For executing processing steps.
      * LLMInterface: For integrating language model functionality.
      * MemoryInterface: For storing and retrieving context.
  
Instructions:
  - Create the following files in `libs/core/langchain-core/`:
      - chain_interface.py
      - llm_interface.py
      - memory_interface.py
  - Use Python’s Abstract Base Classes (ABC) to define required methods.
  - Add detailed docstrings explaining the purpose, expected input, and output.
  - Include hints for logging and error checking in each method.

Example Hint in chain_interface.py:
-------------------------------------
    from abc import ABC, abstractmethod

    class ChainInterface(ABC):
        @abstractmethod
        def run(self, input_data: dict) -> dict:
            """
            Execute the chain of processing steps.
            TODO: Validate the input data, log entry and exit, update the context, and handle errors.
            Hint: Wrap processing in try/except blocks to capture and log exceptions.
            """
            pass

        @abstractmethod
        def add_step(self, step):
            """
            Add a processing step to the chain.
            TODO: Verify that 'step' is callable and log its addition.
            Hint: Use the callable() function to check if step is valid.
            """
            pass

---------------------------------------------------------------------
Task 2: Graph-Based Chain Execution & State Management
---------------------------------------------------------
Objective:
  - Implement a ChainExecutor that organizes processing steps as a Directed Acyclic Graph (DAG).
  - Manage dependencies between steps and execute nodes in topologically sorted order.
  - Integrate a StateManager to maintain global state, support checkpointing, and enable rollback.

Instructions:
  - Create a file `chain_executor.py` in `libs/langchain/langchain/`.
  - Design your ChainExecutor to maintain:
      * A dictionary of nodes (each node is a function representing a processing step).
      * A dependencies dictionary mapping each node to its prerequisite nodes.
      * A reverse-dependency dictionary (to track which nodes depend on a given node).
  - Implement topological sorting (e.g., using Kahn’s algorithm) to resolve execution order.
  - Ensure that before executing each node, a checkpoint of the current state is saved.
  - On node failure, roll back to the previous state.
  - Create a `StateManager` in `state_manager.py` (in the same directory) to handle state operations.

Example Hint in chain_executor.py:
-------------------------------------
    from collections import deque
    from src.core.chain_interface import ChainInterface

    class ChainExecutor(ChainInterface):
        def __init__(self):
            # Initialize dictionaries for nodes and dependencies
            
        def add_node(self, node_id, function, dependencies=None):
            """
            Add a node to the DAG.
            TODO: Validate node_id uniqueness and that function is callable.
            """
            
        def set_state_manager(self, state_manager):
            """
            Attach a StateManager to handle global state.
            """
            

        def run(self, initial_state=None):
            """
            Execute the DAG using topological sorting.
            TODO: Implement Kahn's algorithm for node execution order.
            """
            # Initialize state manager if not provided

---------------------------------------------------------------------
Task 3: Prompt Management
-------------------------
Objective:
  - Develop a PromptTemplate class that dynamically renders templates using variable substitution.
  - Validate that all necessary variables are provided.
  - Design for future extensions such as caching compiled templates or supporting conditional logic.

Instructions:
  - Create `prompt.py` in `libs/langchain/langchain/`.
  - Use Python's `string.Template` for substitution.
  - Add error handling for missing variables.
  
Example Hint:
-------------
    import string

    class PromptTemplate:
        def __init__(self, template: str):
            """
            TODO: Validate that the template contains variable placeholders and store it.
            """
            

        def render(self, **kwargs) -> str:
            """
            Render the template with provided keyword arguments.
            TODO: Use string.Template and handle KeyError for missing variables.
            """
            

---------------------------------------------------------------------
Task 4: Memory and State Management
-------------------------------------
Objective:
  - Create an InMemoryMemory class that implements MemoryInterface.
  - Manage a global state that is updated by each node in the DAG.
  - Support checkpointing and rollback via a StateManager.

Instructions:
  - Create `memory.py` in `libs/langchain/langchain/` and `state_manager.py` in the same directory.
  - In `InMemoryMemory`, use a dictionary to store state.
  - In `StateManager`, implement methods for `get_state()`, `update_state()`, `checkpoint()`, and `rollback()`.

Example Hint (state_manager.py):
-------------------------------
    class StateManager:
        def __init__(self, initial_state=None):
            
        def get_state(self):
            

        def update_state(self, updates):
            

        def checkpoint(self):
           

        def rollback(self):
            

---------------------------------------------------------------------
Task 5: LLM Integration
-----------------------
Objective:
  - Implement a DummyLLM class that simulates language model responses.
  - Allow configuration for delay and error simulation.

Instructions:
  - Create `llm.py` in `libs/langchain/langchain/`.
  - In DummyLLM, simulate response generation with a delay (using time.sleep) and random error generation.

Example Hint:
-------------
    import time, random
    from src.core.llm_interface import LLMInterface

    class DummyLLM(LLMInterface):
        def __init__(self):
            

        def generate(self, prompt: str) -> str:
            

---------------------------------------------------------------------
Task 6: Logging and Debugging
------------------------------
Objective:
  - Develop a Logger module to provide consistent logging across the project.

Instructions:
  - Create `logger.py` in `libs/langchain/langchain/`.
  - Use Python's logging module to configure a logger with a stream handler and formatter.
  - Provide options for adjustable verbosity.

Example Hint:
-------------
    import logging

    def setup_logger(name: str = "langchain", level=logging.DEBUG) -> logging.Logger:
        

---------------------------------------------------------------------
Task 7: Advanced Components – Agent and Tools
-----------------------------------------------
Objective:
  - Implement an Agent class that uses an LLM and ChainExecutor to decide actions.
  - Develop Tool and ToolManager classes to support external integrations.

Instructions:
  - Create `agent.py` and `tools.py` in `libs/langchain/langchain/`.
  - In Agent, implement methods:
      * `decide(input_data: dict) -> str`: Use LLM to generate a decision.
      * `run(input_data: dict) -> dict`: Execute the chain based on the decision.
  - In Tool, define an `execute(query: str)` method.
  - In ToolManager, allow adding tools and executing them by name.

Example Hint (agent.py):
-------------------------
    class Agent:
        def __init__(self, llm, chain_executor):
            # TODO: Store the provided LLM and chain_executor.
            
        def decide(self, input_data: dict) -> str:
            # TODO: Generate a decision prompt and return the LLM response.
            

        def run(self, input_data: dict) -> dict:
            # TODO: Integrate decision logic with chain execution.
            

---------------------------------------------------------------------
Task 8: Command-Line Interface (CLI)
--------------------------------------
Objective:
  - Build a CLI to allow users to run the workflow interactively.

Instructions:
  - Create `cli.py` in `libs/cli/langchain-cli/`.
  - Use argparse to parse command-line arguments.
  - Instantiate ChainExecutor, add sample nodes, and run the workflow.
  - Optionally, demonstrate Agent or ToolManager usage.


---------------------------------------------------------------------
Task 10: Testing and Documentation
------------------------------------
Objective:
  - Write unit and integration tests for all components.
  - Document the design, usage, and extension points in README.md and in the docs/ directory.

Instructions:
  - Create tests in `src/tests/unit/` (e.g., test_prompt.py).
  - Ensure that both normal and edge cases are covered.
  - Update documentation files with clear instructions and examples.

Next Steps:
-----------
1. Use this editorial and the provided TODOs as a guide to build the project.
2. Implement each module and expand the skeleton until you have approximately 700+ lines of code.
3. Test the workflow via the CLI and example application.
4. Update documentation and invite community contributions.

Happy coding and collaborating!
---------------------------------------------------------------------
