"""
Setup tools for pyTheMovieDB.
"""

from setuptools import setup

setup(
    name = 'pyTheMovieDB',
    version = '1.0',
    author = 'Julien Kauffmann',
    author_email = 'julien.kauffmann@freelan.org',
    description = 'A Python wrapper for The Movie Database API (www.themoviedb.org)',
    url = 'http://github.com/ereOn/pythemoviedb',
    license = 'MIT',
    keywords = 'media',

    long_description = """
    Provides access the to The Movie Database API.
    """,

    packages = [
        'pythemoviedb',
        'pythemoviedb.api',
    ],

    entry_points = {
        'console_scripts': [
            'movie-rename = pythemoviedb.main:main',
        ],
    },

    install_requires = [
    ],

    classifiers = [
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Multimedia',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
