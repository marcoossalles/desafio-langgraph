from backend.app.services.external.tmdb.tmdb_service import (
    TMDBService
)


class MovieTools:

    def __init__(self):

        self.tmdb_service = TMDBService()

    async def search_movie(
        self,
        movie_name: str
    ):
        """
        Search for a movie by title.

        Use this tool when the user:
        - mentions a movie
        - asks about a movie
        - wants details about a movie
        - asks for recommendations based on a movie

        Args:
            movie_name: Movie title provided by the user.
        """

        return await (
            self.tmdb_service.search_movie(
                query=movie_name
            )
        )

    async def get_movie_details(
        self,
        movie_id: int
    ):
        """
        Get detailed information about a movie.

        Use this tool when the user asks for:
        - synopsis
        - runtime
        - genres
        - release date
        - rating
        - movie details

        Args:
            movie_id: TMDB movie ID.
        """

        return await (
            self.tmdb_service.get_movie_details(
                movie_id=movie_id
            )
        )

    async def get_movie_credits(
        self,
        movie_id: int
    ):
        """
        Get movie cast and crew information.

        Use this tool when the user asks for:
        - actors
        - cast
        - director
        - crew members

        Args:
            movie_id: TMDB movie ID.
        """

        return await (
            self.tmdb_service.get_movie_credits(
                movie_id=movie_id
            )
        )

    async def get_movie_reviews(
        self,
        movie_id: int
    ):
        """
        Get movie reviews and ratings.

        Use this tool when the user asks for:
        - reviews
        - opinions
        - audience feedback
        - movie ratings

        Args:
            movie_id: TMDB movie ID.
        """

        return await (
            self.tmdb_service.get_movie_reviews(
                movie_id=movie_id
            )
        )

    async def get_movie_videos(
        self,
        movie_id: int
    ):
        """
        Get movie videos and trailers.

        Use this tool when the user asks for:
        - trailers
        - teasers
        - movie videos

        Args:
            movie_id: TMDB movie ID.
        """

        return await (
            self.tmdb_service.get_movie_videos(
                movie_id=movie_id
            )
        )