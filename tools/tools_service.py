"""Business logic for implementing or orchestrating custom Tools. Agents or Chains call these tools behind the scenes."""

import logging
from typing import List


def search_tool(query: str) -> List[str]:
    """
    Example tool that searches an index or external API.

    Args:
        query: The search query string.

    Returns:
        A list of relevant search results matching the given query.

    Raises:
        ValueError: If the query is empty.
    """
    if not query:
        raise ValueError("Query cannot be empty.")

    # TODO: Implement actual search logic here. This might involve calling an external
    # API, running a local index search, or any other form of data retrieval.
    logging.debug("Executing search_tool with query: %s", query)

    results: List[str] = []
    # Placeholder for real search implementation
    # results = ...

    return results


def calculator_tool(expression: str) -> float:
    """
    Example tool that computes math expressions.

    Args:
        expression: A string representing the math expression to compute.

    Returns:
        The computed float value.

    Raises:
        ValueError: If the expression is invalid.
    """
    if not expression:
        raise ValueError("Expression cannot be empty.")

    # TODO: Implement robust math expression parsing and evaluation.
    logging.debug("Executing calculator_tool with expression: %s", expression)

    try:
        result = eval(expression)  # NOTE: eval() is not safe for production use
        return float(result)
    except (SyntaxError, NameError) as exc:
        raise ValueError(f"Invalid expression: {expression}") from exc
    except ZeroDivisionError as exc:
        raise ValueError("Division by zero is not allowed.") from exc