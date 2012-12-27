"""
The pyTheMovieDB "movie-rename" command-line tool.
"""

import pythemoviedb.log
from pythemoviedb.api import *

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

    search_results = methods.search_movie(args.term)
    movie_info = methods.get_movie_all(search_results['results'][0]['id'])
    actors = [item['name'] for item in movie_info['casts']['cast']]

    #import json

    #print json.dumps(movie_info, indent=1)
    print u'\n'.join(actors)

if __name__ == '__main__':
    main()
