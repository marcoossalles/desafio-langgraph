from backend.app.mcp.movie_mcp.tools.movie_tools import (
    MovieTools
)

from backend.app.mcp.movie_mcp.tools.recommendation_tools import (
    RecommendationTools
)


class MovieMCP:

    def __init__(self):

        movie_tools = MovieTools()

        recommendation_tools = (
            RecommendationTools()
        )

        self.tools = {

            "search_movie":
                movie_tools.search_movie,

            "get_movie_details":
                movie_tools.get_movie_details,

            "get_movie_credits":
                movie_tools.get_movie_credits,

            "get_movie_reviews":
                movie_tools.get_movie_reviews,

            "get_movie_videos":
                movie_tools.get_movie_videos,

            "get_similar_movies":
                recommendation_tools
                .get_similar_movies,

            "get_movie_recommendations":
                recommendation_tools
                .get_movie_recommendations
        }

    def get_tools(self):

        return self.tools