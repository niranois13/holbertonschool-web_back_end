#!/usr/bin/env python3
"""
Module of SessionAuth class
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User
from flask import request


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
        try:
            session_id = str(uuid4())
            SessionAuth.user_id_by_session_id.update({session_id: user_id})
            return session_id
        except Exception:
            return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Function that returns a User id based on session_id
        :param session_id: uuid4 - ID of the session we want the User ID from
        Returns:
          - user_id if retrieves, None otherwise
        """
        try:
            return SessionAuth.user_id_by_session_id.get(session_id)
        except Exception:
            return None

    def current_user(self, request=None):
        """
        Function that returns a User id based on cookie value
        :param request: the Flask request object
        Returns:
          - user_id if retrieved, None otherwise
        """
        try:
            session_id = self.session_cookie(request)
            user_id = self.user_id_for_session_id(session_id)
            return User.get(user_id)
        except Exception:
            return None

    def destroy_session(self, request=None):
        """
        Function that destroys a user session, ensuring logout
        :param request: the Flask request object
        Returns:
          - True, on deletion
          - False, otherwise
          """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
