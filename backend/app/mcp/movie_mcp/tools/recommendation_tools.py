from backend.app.services.external.tmdb.tmdb_service import (
    TMDBService
)


class RecommendationTools:

    def __init__(self):

        self.tmdb_service = TMDBService()

    async def get_similar_movies(
        self,
        movie_id: int
    ):
        """
        Get movies similar to another movie.

        Use this tool when the user:
        - wants similar movies
        - asks for movies like another movie
        - asks for related movies

        Args:
            movie_id: TMDB movie ID.
        """

        return await (
            self.tmdb_service.get_movie_similar(
                movie_id=movie_id
            )
        )

    async def get_movie_recommendations(
        self,
        movie_id: int
    ):
        """
        Get movie recommendations based on another movie.

        Use this tool when the user:
        - wants movie recommendations
        - asks what to watch next
        - asks for recommendations based on a movie

        Args:
            movie_id: TMDB movie ID.
        """

        return await (
            self.tmdb_service.get_movie_recommendations(
                movie_id=movie_id
            )
        )