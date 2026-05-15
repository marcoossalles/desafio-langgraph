from backend.app.core.config import settings
from backend.app.core.logger import logger

import httpx


class TMDBService:

    BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self):

        self.headers = {
            "Authorization": f"Bearer {settings.TMDB_API_TOKEN}",
            "Content-Type": "application/json"
        }

    async def _get(self, endpoint: str, params: dict | None = None):

        url = f"{self.BASE_URL}{endpoint}"

        logger.info(
            "tmdb.request.started url=%s params=%s",
            url,
            params
        )

        async with httpx.AsyncClient() as client:

            try:

                response = await client.get(
                    url=url,
                    headers=self.headers,
                    params=params
                )

                response.raise_for_status()

            except httpx.HTTPStatusError:

                logger.exception(
                    "tmdb.request.http_error url=%s params=%s",
                    url,
                    params
                )

                raise

            except httpx.HTTPError:

                logger.exception(
                    "tmdb.request.failed url=%s params=%s",
                    url,
                    params
                )

                raise

            logger.info(
                "tmdb.request.completed url=%s status_code=%s",
                url,
                response.status_code
            )

            return response.json()

    async def search_movie(
        self,
        query: str,
        page: int = 1
    ):

        logger.info("tmdb.movie.search query=%r page=%s", query, page)

        return await self._get(
            endpoint="/search/movie",
            params={
                "query": query,
                "language": "pt-BR",
                "page": page
            }
        )

    async def get_movie_details(
        self,
        movie_id: int
    ):

        logger.info("tmdb.movie.details movie_id=%s", movie_id)

        return await self._get(
            endpoint=f"/movie/{movie_id}",
            params={
                "language": "pt-BR"
            }
        )

    async def get_movie_similar(
        self,
        movie_id: int,
        page: int = 1
    ):

        logger.info(
            "tmdb.movie.similar movie_id=%s page=%s",
            movie_id,
            page
        )

        return await self._get(
            endpoint=f"/movie/{movie_id}/similar",
            params={
                "language": "pt-BR",
                "page": page
            }
        )

    async def get_movie_recommendations(
        self,
        movie_id: int,
        page: int = 1
    ):

        logger.info(
            "tmdb.movie.recommendations movie_id=%s page=%s",
            movie_id,
            page
        )

        return await self._get(
            endpoint=f"/movie/{movie_id}/recommendations",
            params={
                "language": "pt-BR",
                "page": page
            }
        )

    async def get_movie_credits(
        self,
        movie_id: int
    ):

        logger.info("tmdb.movie.credits movie_id=%s", movie_id)

        return await self._get(
            endpoint=f"/movie/{movie_id}/credits",
            params={
                "language": "pt-BR"
            }
        )

    async def get_movie_videos(
        self,
        movie_id: int
    ):

        logger.info("tmdb.movie.videos movie_id=%s", movie_id)

        return await self._get(
            endpoint=f"/movie/{movie_id}/videos",
            params={
                "language": "pt-BR"
            }
        )

    async def get_movie_reviews(
        self,
        movie_id: int,
        page: int = 1
    ):

        logger.info(
            "tmdb.movie.reviews movie_id=%s page=%s",
            movie_id,
            page
        )

        return await self._get(
            endpoint=f"/movie/{movie_id}/reviews",
            params={
                "language": "pt-BR",
                "page": page
            }
        )
