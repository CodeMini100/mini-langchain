import requests

BASE_URL = "http://localhost:8000"


def generate_text(prompt: str, base_url: str = BASE_URL) -> str:
    """
    Calls the /chains/generate_text_endpoint to get LLM output.

    :param prompt: The prompt string used to generate text.
    :param base_url: The base URL of the FastAPI server.
    :return: Generated text from the LLM.
    :raises requests.exceptions.RequestException: If there is a network or server error.
    """
    try:
        response = requests.post(
            f"{base_url}/chains/generate_text_endpoint",
            json={"prompt": prompt}
        )
        response.raise_for_status()
        return response.json().get("text", "")
    except requests.exceptions.RequestException as e:
        # TODO: Log the error and handle it appropriately
        raise e


def agent_query(user_input: str, base_url: str = BASE_URL) -> dict:
    """
    Calls the /agents/agent_query_endpoint to let an agent handle the query.

    :param user_input: The user's query or input for the agent.
    :param base_url: The base URL of the FastAPI server.
    :return: A dictionary containing the agent's response.
    :raises requests.exceptions.RequestException: If there is a network or server error.
    """
    try:
        response = requests.post(
            f"{base_url}/agents/agent_query_endpoint",
            json={"user_input": user_input}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # TODO: Log the error and handle it appropriately
        raise e


def retrieve_memory(session_id: str, base_url: str = BASE_URL) -> dict:
    """
    Demonstrates calling the /memory/get_memory_state_endpoint to retrieve memory state.

    :param session_id: The session ID whose memory state we want to retrieve.
    :param base_url: The base URL of the FastAPI server.
    :return: A dictionary containing the memory state.
    :raises requests.exceptions.RequestException: If there is a network or server error.
    """
    try:
        response = requests.get(
            f"{base_url}/memory/get_memory_state_endpoint",
            params={"session_id": session_id}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # TODO: Log the error and handle it appropriately
        raise e