#!/usr/bin/env python3
"""
Module of SessionAuth class
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    SessionAuth - Class that inherits from base class Auth

    Sets up a Basic Session Authentication system
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Function that creates a Session ID for a user_id:

        1. checks user_id
        2. generates a SessionID as uuid4
        3. the Session ID and user_id are added to user_id_by_session_id dict
        4. returns the sessionID

        :param user_id: ID of a user instance
        Returns:
          - SessionID (uuid4) if generated, None otherwise
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id.update({session_id: user_id})

        return session_id
