from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/tools", tags=["Tools"])


@router.post("/call/{tool_name}")
def call_tool_endpoint(tool_name: str, tool_input: str) -> dict:
    """
    Exposes a REST endpoint to manually trigger a tool.

    Args:
        tool_name (str): The name of the tool to be triggered.
        tool_input (str): The input data required by the tool.

    Returns:
        dict: A dictionary containing information about the tool call and its result.
    """
    try:
        # TODO: Implement logic to call the specified tool using the provided input.
        # For now, return a placeholder response.
        return {
            "tool_name": tool_name,
            "tool_input": tool_input,
            "message": "Tool called successfully"
        }
    except Exception as exc:
        # Handle any unexpected errors during tool invocation
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc)
        ) from exc