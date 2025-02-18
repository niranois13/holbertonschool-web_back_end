#!/usr/bin/env python3
""" Module of Auth base class
"""
from flask import request
from typing import List

class Auth:
    """
    Auth - base class to handle authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth - checks if an API route needs authentication
        :param path: str - routes to be checked for authentication need
        :param excluded_paths: List[str] - route that don't need authentication
        Returns:
          - bool: True if authentication is needed, False otherwise

        Conditions:
          - Returns True if path is None
          - Returns True if excluded_paths is None or empty
          - Normalizes path by ensuring it ends with '/'
          - Returns False if path is found in excluded_paths(including wildcard *)
          - Returns True otherwise
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            elif path == excluded:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header - returns None
        :param request: the Flask request object
        Returns: the Authorization header or None
        """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> str:
        """
        current_user - returns None
        :param request: the Flask request object
        Returns: None
        """
        return None
