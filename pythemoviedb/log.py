"""
The logging module.
"""

import logging

LOGGER = logging.getLogger('pyTheMovieDB')
LOGGER.addHandler(logging.NullHandler())
