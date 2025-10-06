from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.movie import Movie
from ..logging import logger
from .models import MovieResponse

router = APIRouter(prefix="/movies")


@router.get("/", response_model=list[MovieResponse])
async def get_movies(db: DbSession):
    try:
        movies = db.query(Movie).all()
        if not movies:
            logger.warning("No movies found")
            raise HTTPException(status_code=404, detail="No movies found")
    except Exception as e:
        logger.error(f"Error listing movies: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movies_by_id(movie_id: UUID, db: DbSession):
    pass
