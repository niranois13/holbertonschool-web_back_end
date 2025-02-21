#!/usr/bin/env python3
"""
Module of SessionExpAuth class
"""
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth
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
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Creates a user session by associating a user_id and a SessionID
        :param user_id: str - the ID of the user this function
                            creates a sessionID for
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
            }

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retreives a userID from its sessionID
        :param session_id: str - the ID of the session
        Returns:
          - user_id, None otherwise
        """
        if session_id is None:
            return None

        session_dict = self.user_id_by_session_id.get(session_id)

        if session_dict is None:
            return None

        if 'created_at' not in session_dict:
            return None

        if self.session_duration <= 0:
            return session_dict.get('user_id')

        creation_time = session_dict.get('created_at')
        exp_date = creation_time + timedelta(seconds=self.session_duration)

        if exp_date < datetime.now():
            return None

        return session_dict.get('user_id')
