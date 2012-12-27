"""
The configuration module.
"""

import os

API_URL = os.environ.get('PYTHEMOVIEDB_API_URL', 'http://api.themoviedb.org')
API_VERSION = os.environ.get('PYTHEMOVIEDB_API_VERSION', '3')
API_KEY = os.environ.get('PYTHEMOVIEDB_API_KEY')
