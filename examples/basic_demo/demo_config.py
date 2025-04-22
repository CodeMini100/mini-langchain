import os

def load_demo_config() -> None:
    """
    Loads or mocks environment variables for the Flask server.
    Missing variables are set to default values.

    Raises:
        OSError: If an error occurs while loading environment variables.
    """
    try:
        # TODO: Consider loading real environment variables from a .env file or another secure source
        if not os.getenv("LANGCHAIN_MVP_API_URL"):
            os.environ["LANGCHAIN_MVP_API_URL"] = "http://localhost:8000"
    except Exception as err:
        raise OSError("Error loading environment variables.") from err


def get_langchain_mvp_api_url() -> str:
    """
    Returns the base URL of the FastAPI app.

    Returns:
        str: The base URL for the FastAPI server.
    """
    return os.getenv("LANGCHAIN_MVP_API_URL", "http://localhost:8000")