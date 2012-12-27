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

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig()
        pythemoviedb.log.LOGGER.setLevel(logging.DEBUG)

    from pythemoviedb.api import *

    print repr(get_movie(74534))
    print repr(get_movie(74534, 'fr'))
    print repr(get_movie_alternative_titles(74534))
    print repr(get_movie_alternative_titles(74534, 'FR'))
    print repr(get_movie_casts(74534))

if __name__ == '__main__':
    main()
