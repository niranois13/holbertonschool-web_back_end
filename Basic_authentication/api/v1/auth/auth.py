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
        :param excluded_path: List[str] - routes that don't need authentication
        Returns: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization_header - returns None
        :param request: the Flask request object
        Returns: None
        """
        return None

    def current_user(self, request=None) -> str:
        """
        current_user - returns None
        :param request: the Flask request object
        Returns: None
        """
        return None
