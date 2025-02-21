#!/usr/bin/env python3
"""
Module of SessionExpAuth class
"""
from datetime import datetime, timedelta
from api.v1.auth.auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    Class that inherits from SessionAuth - Adds expiration date to a SessionID
    """
    def __init__(self):
        """
        SessionExpAuth initialization
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Creates a user session by associating a user_id and a SessionID
        :param user_id: str - the ID of the user this function creates a sessionID for
        """
        try:
            session_id = super().create_session(user_id)

            SessionExpAuth.user_id_by_session_id = {
            "user_id": user_id,
            "created_at": datetime.now()
            }

            return session_id

        except Exception:
            return None

    def user_id_for_session_id(self, session_id=None):
        """
        Retreives a userID from its sessionID
        :param session_id: str - the ID of the session
        Returns:
          - user_id, None otherwise
        """
        if not session_id:
            return None

        session_dict = SessionExpAuth.user_id_by_session_id.get(
            session_id, None
            )

        if not session_dict:
            return None

        if not session_dict.get('created_at'):
            return None
        
        if self.session_duration <= 0:
            return session_dict.get('user_id')

        creation_time = session_dict.get('created_at')
        session_time = timedelta(seconds=self.session_duration)
        expiration_date = creation_time + session_time

        if expiration_date < datetime.now():
            return None

        return session_dict.get('user_id')

