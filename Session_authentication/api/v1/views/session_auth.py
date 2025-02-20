#!/usr/bin/env python3
"""
Authentication views
"""
from api.v1.views import app_views
from typing import TypeVar
from os import getenv
from flask import request, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Function that handles user login
    :param request: Flask request object
    Returns:
        - User instance
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({ "error": "no user found for this email" }), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({ "error": "wrong password" }), 401
        else:
            from api.v1.app import auth
            current_user = users[0]
            session_id = auth.create_session(current_user.id)
            SESSION_NAME = getenv('SESSION_NAME')

            response = jsonify(user.to_json())
            response.set_cookie(SESSION_NAME, session_id)

            return response
