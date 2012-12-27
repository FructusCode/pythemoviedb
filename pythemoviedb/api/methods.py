"""
The API methods.
"""

import pythemoviedb.configuration as configuration
from pythemoviedb.log import LOGGER

import urllib
import urllib2
import urlparse
import json

def make_request(action, parameters=None, base_url=configuration.API_URL, api_version=configuration.API_VERSION, api_key=configuration.API_KEY):
    """
    Make a request to the server.
    """

    if not api_key:
        raise RuntimeError('No API key defined. Request would fail.')

    def stringify_value(value):

        if value is True:
            return 'true'
        elif value is False:
            return 'false'

        return str(value)

    query_string = dict((key, stringify_value(value)) for key, value in (parameters or {}).items() if value is not None)

    query_string.update({
        'api_key': api_key,
    })

    url = urlparse.urljoin(base_url, '/'.join([api_version, action])) + '?' + urllib.urlencode(query_string)
    request = urllib2.Request(url)
    request.add_header('Accept', 'application/json')

    LOGGER.debug('Making request to %s', request.get_full_url())

    class APIHandler(urllib2.BaseHandler):
        """
        A HTTP error handler.
        """

        def http_error_401(self, request, response, code, msg, hdrs):
            """
            Handles 401 errors.
            """

            data = json.loads(response.read())

            raise APIError(**data)

        http_error_404 = http_error_401

    api_handler = urllib2.build_opener(APIHandler)

    response = api_handler.open(request)

    return json.loads(response.read())

def parse_datetime(date):
    """
    Parse a date in the API format.

    :param date: The date to parse.
    :returns: A Python datetime.DateTime instance.
    """

    import datetime

    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S %Z')

def format_date(date):
    """
    Format a date in the API format.

    :param date: The date to format.
    :returns: An API formatted date.
    """

    if date:
        return date.format('%Y-%m-%d')

def get_configuration():
    """
    Get the configuration.

    :returns: The configuration as a dictionary.
    """

    return make_request('configuration')

def get_authentication_token():
    """
    Request an authentication token.

    :returns: The authentication token.
    """

    return make_request('authentication/token/new')

def new_session(request_token):
    """
    Request a new session.

    :param request_token: The request token.
    :returns: The session.
    """

    return make_request('authentication/session/new', {
        'request_token': request_token,
    })

def new_guest_session():
    """
    Request a new guest session.

    :returns: The session.
    """

    return make_request('authentication/guest_session/new')

def get_movie(_id, language=None, append_to_response=None):
    """
    Get the movie that has the specified identifier.

    :param _id: The movie identifier.
    :param language: The language as a ISO 639-1 code.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie if it exists.
    """

    return make_request('movie/%s' % _id, parameters={
        'language': language,
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_all(_id, language=None, country=None):
    """
    Get the movie that has the specified identifier with all the possible information.

    :param _id: The movie identifier.
    :param language: The language as a ISO 639-1 code.
    :param country: The country as an ISO 3166-1 code.
    :returns: The movie if it exists.
    """

    append_to_response = [
        'alternative_titles',
        'casts',
        'images',
        'keywords',
        'releases',
        'trailers',
        'translations',
        'similar_movies',
        'lists',
    ]

    return make_request('movie/%s' % _id, parameters={
        'language': language,
        'country': country,
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_alternative_titles(_id, country=None, append_to_response=None):
    """
    Get a movie alternative titles.

    :param _id: The movie identifier.
    :param country: The country as an ISO 3166-1 code.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie alternative titles if it exists.
    """

    return make_request('movie/%s/alternative_titles' % _id, parameters={
        'country': country,
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_casts(_id, append_to_response=None):
    """
    Get a movie casts.

    :param _id: The movie identifier.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie casts if it exists.
    """

    return make_request('movie/%s/casts' % _id, parameters={
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_images(_id, language=None, append_to_response=None):
    """
    Get a movie images.

    :param _id: The movie identifier.
    :param language: The language as a ISO 639-1 code.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie if it exists.
    """

    return make_request('movie/%s/images' % _id, parameters={
        'language': language,
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_keywords(_id, append_to_response=None):
    """
    Get a movie keywords.

    :param _id: The movie identifier.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie keywords if it exists.
    """

    return make_request('movie/%s/keywords' % _id, parameters={
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_releases(_id, append_to_response=None):
    """
    Get a movie releases.

    :param _id: The movie identifier.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie releases if it exists.
    """

    return make_request('movie/%s/releases' % _id, parameters={
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_trailers(_id, append_to_response=None):
    """
    Get a movie trailers.

    :param _id: The movie identifier.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie trailers if it exists.
    """

    return make_request('movie/%s/trailers' % _id, parameters={
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_translations(_id, append_to_response=None):
    """
    Get a movie translations.

    :param _id: The movie identifier.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie translations if it exists.
    """

    return make_request('movie/%s/translations' % _id, parameters={
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_similar_movies(_id, language=None, append_to_response=None):
    """
    Get a movie similar :movies.

    :param _id: The movie identifier.
    :param language: The language as a ISO 639-1 code.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie similar movies if it exists.
    """

    return make_request('movie/%s/similar_movies' % _id, parameters={
        'language': language,
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_lists(_id, language=None, append_to_response=None):
    """
    Get a movie lists.

    :param _id: The movie identifier.
    :param language: The language as a ISO 639-1 code.
    :param append_to_response: A list of additinal methods to append to the response.
    :returns: The movie lists if it exists.
    """

    return make_request('movie/%s/lists' % _id, parameters={
        'language': language,
        'append_to_response': append_to_response and ','.join(append_to_response) or None,
    })

def get_movie_changes(_id, start_date=None, stop_date=None):
    """
    Get a movie changes.

    :param _id: The movie identifier.
    :param start_date: The start date for changes.
    :param stop_date: The stop date for changes.
    :returns: The movie changes if it exists.
    """

    return make_request('movie/%s/changes' % _id, parameters={
        'start_date': format_date(start_date),
        'stop_date': format_date(stop_date),
    })

def get_latest_movie():
    """
    Get the latest movie identifier.

    :returns: The latest movie.
    """

    return make_request('movie/latest')

def get_upcoming_movies(page=None, language=None):
    """
    Get a list of the upcoming movies.

    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The upcoming movies.
    """

    return make_request('movie/upcoming', parameters={
        'page': page,
        'language': language,
    })

def get_now_playing_movies(page=None, language=None):
    """
    Get a list of the now playing movies.

    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The now playing movies.
    """

    return make_request('movie/now_playing', parameters={
        'page': page,
        'language': language,
    })

def get_popular_movies(page=None, language=None):
    """
    Get a list of the popular movies.

    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The popular movies.
    """

    return make_request('movie/popular', parameters={
        'page': page,
        'language': language,
    })

def get_top_rated_movies(page=None, language=None):
    """
    Get a list of the top rated movies.

    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The top rated movies.
    """

    return make_request('movie/top_rated', parameters={
        'page': page,
        'language': language,
    })

def set_movie_rating(_id, rating):
    """
    Set the rating of a movie.

    :param _id: The movie identifier.
    :param rating: The rating.
    """

    raise NotImplementedError()

def get_collection(_id, language=None):
    """
    Get a collection.

    :param _id: The collection identifier.
    :param language: The language as a ISO 639-1 code.
    :returns: The collection.
    """

    return make_request('collection/%s' % _id, parameters={
        'language': language,
    })

def get_collection_images(_id, language=None):
    """
    Get a collection images.

    :param _id: The collection identifier.
    :param language: The language as a ISO 639-1 code.
    :returns: The collection images.
    """

    return make_request('collection/%s/images' % _id, parameters={
        'language': language,
    })

def get_person(_id):
    """
    Get the person that has the specified id.

    :param _id: The person identifier.
    :returns: The person.
    """

    return make_request('person/%s' % _id)

def get_person_credits(_id, language=None):
    """
    Get a person credits.

    :param _id: The person identifier.
    :param language: The language as a ISO 639-1 code.
    :returns: The person credits.
    """

    return make_request('person/%s/credits' % _id, parameters={
        'language': language,
    })

def get_person_images(_id):
    """
    Get a person images.

    :param _id: The person identifier.
    :returns: The person images.
    """

    return make_request('person/%s/images' % _id)

def get_person_changes(_id, start_date=None, stop_date=None):
    """
    Get a person changes.

    :param _id: The person identifier.
    :param start_date: The start date for changes.
    :param stop_date: The stop date for changes.
    :returns: The person changes if it exists.
    """

    return make_request('person/%s/changes' % _id, parameters={
        'start_date': format_date(start_date),
        'stop_date': format_date(stop_date),
    })

def get_latest_person():
    """
    Get the latest person identifier.

    :returns: The latest person identifier.
    """

    return make_request('person/latest')

def get_list(_id):
    """
    Get the list that has the specified id.

    :param _id: The list identifier.
    :returns: The list.
    """

    return make_request('list/%s' % _id)

def get_company(_id):
    """
    Get the company that has the specified id.

    :param _id: The company identifier.
    :returns: The company.
    """

    return make_request('company/%s' % _id)

def get_company_movies(_id, page=None, language=None):
    """
    Get a company movies.

    :param _id: The company identifier.
    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The company movies.
    """

    return make_request('company/%s/movies' % _id, parameters={
        'page': page,
        'language': language,
    })

def get_genres(language=None):
    """
    Get a list of the genres.

    :param language: The language as a ISO 639-1 code.
    :returns: The genres list.
    """

    return make_request('genre/list', parameters={
        'language': language,
    })

def get_movies_by_genre(_id, page=None, language=None, include_all_movies=False):
    """
    Get a list of all the movies of the specified genre.

    :param _id: The genre identifier.
    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :param include_all_movies: Whether to include all movies in the result or just the ones that were voted-up at least 10 times.
    :returns: The movies list.
    """

    return make_request('genre/%s/movies' % _id, parameters={
        'page': page,
        'language': language,
        'include_all_movies': include_all_movies,
    })

def get_keyword(_id):
    """
    Get the keyword that has the specified id.

    :param _id: The keyword identifier.
    :returns: The keyword.
    """

    return make_request('keyword/%s' % _id)

def get_movies_by_keyword(_id, page=None, language=None):
    """
    Get a list of all the movies that have the specified keyword.

    :param _id: The genre identifier.
    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The movies list.
    """

    return make_request('keyword/%s/movies' % _id, parameters={
        'page': page,
        'language': language,
    })

def search_movie(query, page=None, language=None, include_adult=False, year=None):
    """
    Search for a movie.

    :param query: The search query.
    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :param include_adult: Whether to include adult movies in the result.
    :param year: Limit search to a specific year.
    :returns: The movies list.
    """

    return make_request('search/movie', parameters={
        'query': query,
        'page': page,
        'language': language,
        'include_adult': include_adult,
        'year': year,
    })

def search_collection(query, page=None, language=None):
    """
    Search for a collection.

    :param query: The search query.
    :param page: The page to show.
    :param language: The language as a ISO 639-1 code.
    :returns: The collections list.
    """

    return make_request('search/collection', parameters={
        'query': query,
        'page': page,
        'language': language,
    })

def search_person(query, page=None, include_adult=False):
    """
    Search for a person.

    :param query: The search query.
    :param page: The page to show.
    :param include_adult: Whether to include adult movies in the result.
    :returns: The persons list.
    """

    return make_request('search/person', parameters={
        'query': query,
        'page': page,
        'include_adult': include_adult,
    })

def search_list(query, page=None, include_adult=False):
    """
    Search for a list.

    :param query: The search query.
    :param page: The page to show.
    :param include_adult: Whether to include adult movies in the result.
    :returns: The lists list.
    """

    return make_request('search/list', parameters={
        'query': query,
        'page': page,
        'include_adult': include_adult,
    })

def search_company(query, page=None):
    """
    Search for a company.

    :param query: The search query.
    :param page: The page to show.
    :returns: The companies list.
    """

    return make_request('search/company', parameters={
        'query': query,
        'page': page,
    })

def search_keyword(query, page=None):
    """
    Search for a keyword.

    :param query: The search query.
    :param page: The page to show.
    :returns: The keywords list.
    """

    return make_request('search/keyword', parameters={
        'query': query,
        'page': page,
    })

def get_changed_movies(page=None, start_date=None, stop_date=None):
    """
    Get the list of changed movies.

    :param page: The page to show.
    :param start_date: The start date for changes.
    :param stop_date: The stop date for changes.
    :returns: The list of changed movies.
    """

    return make_request('movie/changes', parameters={
        'page': page,
        'start_date': format_date(start_date),
        'stop_date': format_date(stop_date),
    })

def get_changed_persons(page=None, start_date=None, stop_date=None):
    """
    Get the list of changed persons.

    :param page: The page to show.
    :param start_date: The start date for changes.
    :param stop_date: The stop date for changes.
    :returns: The list of changed persons.
    """

    return make_request('person/changes', parameters={
        'page': page,
        'start_date': format_date(start_date),
        'stop_date': format_date(stop_date),
    })
