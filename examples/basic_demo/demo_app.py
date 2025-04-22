import logging
from flask import Flask, request, jsonify
from typing import Any

# TODO: Adjust the import as needed depending on actual file/module structure
from . import demo_api


def create_flask_app() -> Flask:
    """
    Initializes and configures the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/", methods=["GET"])
    def serve_frontend() -> Any:
        """
        Placeholder endpoint to serve the React frontend.

        Returns:
            Any: A placeholder response indicating the React front end route.
        """
        # TODO: Implement actual serving of React static files
        return "React application is served here."

    @app.route("/api/demo", methods=["GET"])
    def demo_endpoint() -> Any:
        """
        Endpoint that demonstrates calling backend logic from demo_api.

        Returns:
            Any: JSON response from the demo API or an error message.
        """
        try:
            result = demo_api.demo_function()
            return jsonify({"data": result}), 200
        except Exception as error:
            app.logger.error("An error occurred: %s", error)
            return jsonify({"error": str(error)}), 500

    @app.errorhandler(404)
    def not_found_handler(error: Exception) -> Any:
        """
        Handler for 404 Not Found errors.

        Args:
            error (Exception): The exception raised for a 404 error.

        Returns:
            Any: JSON response with an error message and status code.
        """
        return jsonify({"error": "Not Found"}), 404

    return app


def run_demo_app() -> None:
    """
    Runs the Flask application on a specified port.

    Returns:
        None
    """
    app = create_flask_app()
    # TODO: Make the port and debug mode configurable if needed
    app.run(host="0.0.0.0", port=5000, debug=False)


if __name__ == "__main__":
    run_demo_app()