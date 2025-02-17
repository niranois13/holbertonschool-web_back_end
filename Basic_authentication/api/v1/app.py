#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def auth_handler():
    """
    Authentication handler executed before each request.

    This function performs the following checks:
    1. If auth is None, no authentication is required.
    2. Checks if the request path requires authentication.
    3. Verifies the presence of a valid authorization header.
    4. Confirms the existence of a current user.

    The function will abort the request with appropriate HTTP status codes
    if authentication fails at any step.

    Excluded paths:
    - '/api/v1/status/'
    - '/api/v1/unauthorized/'
    - '/api/v1/forbidden/'

    Raises:
        401 Unauthorized: If the authorization header is missing or invalid.
        403 Forbidden: If there is no current user associated with the request.

    Returns:
        None
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
        ]
    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({
        "error": "Forbidden"
        }), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
