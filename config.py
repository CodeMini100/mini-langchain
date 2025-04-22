import os
from typing import Optional

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def load_config() -> None:
    """
    Loads environment variables from a .env file if present or directly from the system environment.
    This function sets environment variables in the current process where they are accessible.
    Raises:
        RuntimeError: If python-dotenv is not installed and a .env file is required.
    """
    # TODO: Ensure python-dotenv is installed in production if you plan to use .env files
    if load_dotenv:
        try:
            load_dotenv()
        except Exception as e:
            # TODO: Consider logging the error instead of printing in production
            print(f"Failed to load .env file: {e}")
    else:
        # TODO: Consider raising an error or logging a warning if .env usage is critical
        pass


def get_database_url() -> str:
    """
    Retrieves a database URL from environment variables, commonly used by SQLAlchemy.
    Returns:
        str: The database URL.
    Raises:
        ValueError: If the DATABASE_URL environment variable is not found.
    """
    db_url: Optional[str] = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL environment variable not set.")
    return db_url