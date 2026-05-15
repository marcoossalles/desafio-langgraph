from pydantic import BaseModel
from typing import Optional


class MovieResponse(BaseModel):

    id: int

    title: str

    overview: Optional[str]

    release_date: Optional[str]

    vote_average: float