import uvicorn
from fastapi import FastAPI

def create_app() -> FastAPI:
    """
    Initializes and configures the FastAPI application.

    Returns:
        FastAPI: A FastAPI application instance with necessary routers mounted.
    """
    app = FastAPI(title="LangChain_MVP")
    # TODO: Include routers from chains, agents, etc.
    # Example: app.include_router(chains.router, prefix="/chains", tags=["chains"])
    # Example: app.include_router(agents.router, prefix="/agents", tags=["agents"])
    return app

def run_app() -> None:
    """
    Launches the server using uvicorn. Intended for use when not running via the CLI.
    """
    try:
        uvicorn.run("main:create_app", host="0.0.0.0", port=8000, reload=True)
    except Exception as error:
        # Logging can be handled here in production code
        print(f"Failed to start server: {error}")