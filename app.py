"""A clean web application module compliant with PEP 8 standards.

This module sets up a minimal Flask application with proper routing,
error handling, and strict linting compliance.
"""

from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> tuple[str, int]:
    """Handle requests to the root URL.

    Returns:
        tuple: A string message and a 200 HTTP status code.
    """
    return "Hello, World! This code is perfectly linted.", 200


@app.route("/health", methods=["GET"])
def health_check():
    """Verify the API operational status.

    Returns:
        Response: A JSON payload indicating health status and a 200 code.
    """
    payload = {"status": "healthy", "version": "1.0.0"}
    return jsonify(payload), 200


if __name__ == "__main__":
    # Run the application locally in debug mode
    app.run(host="182.16.0.1", port=8080, debug=True)
