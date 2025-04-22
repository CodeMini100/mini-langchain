"""Business logic for building/maintaining LangChain 'Chain' objects, including prompt templates and flow definitions."""

from typing import Any
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def build_simple_chain(llm_provider: Any) -> LLMChain:
    """
    Returns a basic LangChain chain instance with a single prompt step.

    :param llm_provider: The language model provider to use for building the chain.
    :type llm_provider: Any
    :raises ValueError: If the provided llm_provider is None.
    :return: A LangChain chain with one prompt step.
    :rtype: LLMChain
    """
    if llm_provider is None:
        raise ValueError("llm_provider cannot be None")

    prompt = PromptTemplate(
        input_variables=["user_input"],
        template="You are a helpful assistant. Please answer the following question: {user_input}"
    )

    chain = LLMChain(
        llm=llm_provider,
        prompt=prompt
    )

    # TODO: Add error handling for unexpected model behavior.
    # TODO: Extend this chain with additional steps or logic as needed.

    return chain