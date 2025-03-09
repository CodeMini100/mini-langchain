"""
Example demonstrating the LangChain-lite framework.

This example builds a chain that:
  - Uses a PromptTemplate to generate a prompt.
  - Uses a DummyLLM to simulate a text generation response.
  - Processes the LLM response and stores the result in memory.
  - Optionally demonstrates usage of an Agent to make decisions and a ToolManager for external tool stubs.
  
The final chain context and outputs are logged and printed.
"""

from libs.langchain.langchain.chain_executor import ChainExecutor
from libs.langchain.langchain.prompt import PromptTemplate
from libs.langchain.langchain.llm import DummyLLM
from libs.langchain.langchain.memory import InMemoryMemory
from libs.langchain.langchain.logger import setup_logger
from libs.langchain.langchain.agent import Agent
from libs.langchain.langchain.tools import Tool, ToolManager

def main():
    # Set up logging
    logger = setup_logger("example")
    logger.info("Starting LangChain-lite Example")

    # Initialize a ChainExecutor instance
    executor = ChainExecutor()

    # Define a chain step: Render a prompt and generate an LLM response.
    def llm_step(context: dict) -> dict:
        # Render a prompt using the input subject.
        prompt_template = PromptTemplate("Tell me something interesting about $subject.")
        subject = context.get("subject", "AI")
        try:
            rendered_prompt = prompt_template.render(subject=subject)
        except Exception as e:
            logger.error(f"Error rendering prompt: {e}")
            rendered_prompt = "Default prompt"
        logger.info(f"Rendered Prompt: {rendered_prompt}")

        # Get a simulated response from the DummyLLM.
        llm = DummyLLM()
        try:
            llm_response = llm.generate(rendered_prompt)
        except Exception as e:
            logger.error(f"Error generating LLM response: {e}")
            llm_response = "Error in LLM response"
        logger.info(f"LLM Response: {llm_response}")
        return {"llm_response": llm_response}

    # Define a chain step: Process the LLM response and save it in memory.
    def process_step(context: dict) -> dict:
        response = context.get("llm_response", "")
        processed = response + " [processed]"
        logger.info(f"Processed Output: {processed}")

        # Save the processed output into memory.
        memory = InMemoryMemory()
        memory.save({"processed_output": processed})
        current_memory = memory.load()
        logger.info(f"Memory Content: {current_memory}")
        return {"processed_output": processed}

    # Add steps to the chain executor.
    executor.add_step(llm_step)
    executor.add_step(process_step)

    # Run the chain with initial input.
    initial_input = {"subject": "LangChain"}
    final_context = executor.run(initial_input)
    logger.info(f"Final Chain Context: {final_context}")

    # Optionally, demonstrate Agent usage.
    agent = Agent(DummyLLM(), executor)
    try:
        decision = agent.decide({"subject": "Advanced topic"})
        logger.info(f"Agent Decision: {decision}")
        agent_context = agent.run({"subject": "Agent input"})
        logger.info(f"Agent Chain Context: {agent_context}")
    except Exception as e:
        logger.error(f"Agent error: {e}")

    # Optionally, demonstrate ToolManager usage.
    tool_manager = ToolManager()
    sample_tool = Tool("SearchTool")
    tool_manager.add_tool(sample_tool)
    try:
        tool_result = tool_manager.execute_tool("SearchTool", "query about LangChain")
        logger.info(f"Tool Result: {tool_result}")
    except Exception as e:
        logger.error(f"Tool execution error: {e}")

if __name__ == "__main__":
    main()
