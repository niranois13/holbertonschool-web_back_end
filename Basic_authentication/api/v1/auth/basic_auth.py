#!/usr/bin/env python3
"""
Module of BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth - Class that inherits from base class Auth

    Sets up a Basic Authentication system
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Function that return the Base64 part of the Authorization header
        :param authorization_header: str -
                            the authorization header to be manipulated
        Returns:
          - The base64 part of the Authorization header if properly formatted
          - None otherwise
        """
        if authorization_header is None or not isinstance(
                                    authorization_header, str):
            return None

        base64_part = authorization_header.removeprefix(
            'Basic ') if authorization_header.startswith(
                'Basic ') else None

        return base64_part

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Function that decodes a base64 authorization header
        :param base_64_authorization_header: str - base64 string to be decoded
        Returns:
          - The decoded authorization header if properly formatted
          - None otherwise
        """
        if base64_authorization_header is None or not isinstance(
                                    base64_authorization_header, str):
            return None

        try:
            decoded_authorization_header = base64.b64decode(
                                    base64_authorization_header, validate=True)
            return decoded_authorization_header.decode("UTF-8")
        except Exception:
            return None
