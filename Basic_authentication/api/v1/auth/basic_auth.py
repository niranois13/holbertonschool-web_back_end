#!/usr/bin/env python3
"""
Module of BasicAuth class
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> tuple[str, str]:
        """
        Function extracts an user email and password from
        a decoded base64 authorization header
        :param decoded_base64_authorization_header: str - the header user
                                    credentials should be extracted from
        Returns:
          - a tuple containing user email and password,
          - None otherwise
        """
        if decoded_base64_authorization_header is None or not isinstance(
                                    decoded_base64_authorization_header, str):
            return (None, None)

        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
                    self, user_email: str, user_pwd: str) -> User:
        """
        Function that returns a User instance based on its credentials
        :param user_email: str - email of an user
        :param user_pwd: str - password of an user
        Returns:
          - the User instance associated to the credentials
          - None otherwise
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})

        if not users or len(users) == 0:
            return None

        user_instance = users[0]

        if not user_instance.is_valid_password(user_pwd):
            return None

        return user_instance
