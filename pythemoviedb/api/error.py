"""
The API error classes and functions.
"""

from functools import wraps

class APIError(Exception):
    """
    An API exception class.
    """

    SUCCESS = 1
    INVALID_SERVICE = 2
    AUTHENTICATION_FAILED = 3
    INVALID_FORMAT = 4
    INVALID_PARAMETERS = 5
    INVALID_ID = 6
    INVALID_API_KEY = 7
    DUPLICATE_ENTRY = 8
    SERVICE_OFFLINE = 9
    SUSPENDED_API_KEY = 10
    INTERNAL_ERROR = 11

    def __init__(self, status_code, status_message):
        """
        Create an API exception.

        :param msg: The message.
        :param status_code: The status code, as received in the API response.
        :param status_message: The status message, as received in the API response.
        """

        super(APIError, self).__init__('%s (error %s)' % (status_message, status_code))

        self.status_code = status_code
        self.status_message = status_message

    @staticmethod
    def silent_error(status_code, default_return_value=None):
        """
        A decorator that silence some errors.
        """

        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kw):
                try:
                    return f(*args, **kw)

                except APIError as ex:

                    if ex.status_code == status_code:
                        return default_return_value

                    else:
                        raise

            return wrapper

        return decorator
