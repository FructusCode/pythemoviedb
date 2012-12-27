"""
The API objects classes.
"""

class AuthenticationToken(object):
    """
    An authentication token.
    """

    def __init__(self, request_token, expires_at):
        """
        Create an authentication token.
        """

        self.request_token = request_token
        self.expires_at = expires_at

    def __str__(self):
        """
        Get a string representation of the AuthenticationToken.
        """

        return self.request_token

    def __repr__(self):
        """
        Get a Python representation of the AuthenticationToken.
        """

        return '%s(%s)' % (
            self.__class__,
            ', '.join('%s=%r' % item for item in self.__dict__.items()),
        )

class Session(object):
    """
    An session.
    """

    def __init__(self, session_id, expires_at):
        """
        Create a session.
        """

        self.session_id = session_id
        self.expires_at = expires_at

    def __str__(self):
        """
        Get a string representation of the Session.
        """

        return self.session_id

    def __repr__(self):
        """
        Get a Python representation of the Session.
        """

        return '%s(%s)' % (
            self.__class__,
            ', '.join('%s=%r' % item for item in self.__dict__.items()),
        )

class GuestSession(object):
    """
    An session.
    """

    def __init__(self, guest_session_id, expires_at):
        """
        Create a guest session.
        """

        self.guest_session_id = guest_session_id
        self.expires_at = expires_at

    def __str__(self):
        """
        Get a string representation of the GuestSession.
        """

        return self.guest_session_id

    def __repr__(self):
        """
        Get a Python representation of the GuestSession.
        """

        return '%s(%s)' % (
            self.__class__,
            ', '.join('%s=%r' % item for item in self.__dict__.items()),
        )
