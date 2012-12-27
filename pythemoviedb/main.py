"""
The pyTheMovieDB "movie-rename" command-line tool.
"""

import pythemoviedb.log

import argparse
import logging

def main():
    """
    The command-line tool entry point.
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
    parser.add_argument('term', help='The search term')

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig()
        pythemoviedb.log.LOGGER.setLevel(logging.DEBUG)

    from pythemoviedb.api import *

    print methods.get_movie(550)
    print methods.get_movie_alternative_titles(550)

if __name__ == '__main__':
    main()
