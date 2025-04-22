from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Dict
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/chains",
    tags=["Chains"]
)


class GenerateTextRequest(BaseModel):
    """
    Request model containing the user input.
    """
    user_input: str


@router.post("/generate", response_model=Dict[str, str])
def generate_text_endpoint(request_data: GenerateTextRequest) -> Dict[str, str]:
    """
    Accepts user input, passes it to a chain, and returns the LLM-generated output.

    :param request_data: The request model containing user input.
    :return: A dictionary containing the generated text.
    """
    try:
        # TODO: Implement chain logic here (e.g., call an external LLM service or local chain function)
        # Placeholder for chain output
        chain_output = f"Echo: {request_data.user_input}"

        return {"generated_text": chain_output}
    except Exception as e:
        logger.error("Error in generate_text_endpoint: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while generating text."
        )