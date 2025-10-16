from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.movie import Movie
from ..logging import logger
from .models import MovieCreate, MovieResponse

router = APIRouter(prefix="/movies")


@router.get("/", response_model=list[MovieResponse])
async def get_movies(db: DbSession):
    movies = db.query(Movie).all()
    if not movies:
        raise HTTPException(status_code=404, detail="No movies found")
    return movies


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movies_by_id(movie_id: UUID, db: DbSession):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail=f"No movie found for ID: {movie_id}")
    logger.info(f"Found Movie for ID: {movie_id}")
    return movie


@router.post("/create", response_model=MovieResponse)
async def create_movie(movie: MovieCreate, db: DbSession):
    try:
        logger.info(f"Data received: {movie.model_dump()}")
        new_movie = Movie(**movie.model_dump())
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)

        logger.info(f"Movie created with ID: {new_movie.id}")
        return MovieResponse.model_validate(new_movie)

    except Exception as e:
        logger.error(f"Error creating new movie: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
