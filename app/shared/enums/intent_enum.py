from enum import Enum


class IntentEnum(str, Enum):

    MOVIE_SEARCH = "movie_search"

    MOVIE_DETAILS = "movie_details"

    MOVIE_RECOMMENDATION = "movie_recommendation"

    UNKNOWN = "unknown"