from typing import Optional
from pydantic import BaseModel, Field, validator

"""
Pydantic models for request/response data related to chain usage.
"""


class ChainRequest(BaseModel):
    """
    Model for user prompt data and chain configuration requests.
    """

    user_input: str = Field(..., description="The user's prompt or query.")
    chain_name: str = Field(..., description="The name of the chain to be used.")
    # TODO: Add additional fields or nested models as needed

    @validator("user_input")
    def validate_user_input(cls, value: str) -> str:
        """
        Validate that user_input is not empty.

        Raises:
            ValueError: If user_input is empty.

        Returns:
            str: The validated user_input.
        """
        if not value.strip():
            raise ValueError("User input cannot be empty.")
        return value


class ChainResponse(BaseModel):
    """
    Model for chain response data.
    """

    output: str = Field(..., description="The chain's response or result.")
    success: bool = Field(True, description="Indicates if the chain execution was successful.")
    error_message: Optional[str] = Field(None, description="Contains an error message if chain execution fails.")
    # TODO: Extend with additional fields or nested models as needed