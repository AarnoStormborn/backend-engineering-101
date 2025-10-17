# list all shows
# list show by id
# filter shows
# create bookings

from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.movie import Movie
from ..db.entities.show import Show
from ..db.entities.theater import Theater
from ..logging import logger
from .models import ShowCreate, ShowResponse

router = APIRouter(prefix="/shows")


@router.get("/")
async def get_shows(db: DbSession):
    shows = db.query(Show).all()
    if not shows:
        raise HTTPException(status_code=404, detail="No Shows found")
    logger.info(f"Shows found: {len(shows)}")
    return shows


@router.get("/{show_id}")
async def get_show_by_id(show_id: UUID, db: DbSession):
    show = db.query(Show).filter(Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=400, detail=f"No Shows found for ID: {show_id}")
    logger.info(f"Show found for ID: {show_id}")
    return show


@router.get("/filter")
async def filter_shows(db: DbSession, movie_id: UUID = None, theater_id: UUID = None):
    shows = db.query(Show).filter(Theater.id == theater_id).filter(Movie.id == movie_id).all()
    if not shows:
        raise HTTPException(status_code=404, detail="No shows for specified filters")
    logger.info(f"Shows found: {len(shows)}")
    return shows


@router.post("/create")
async def create_bookings(show: ShowCreate, db: DbSession):
    try:
        logger.info(f"Data received: {show.model_dump()}")
        new_show = Show(**show.model_dump())
        db.add(new_show)
        db.commit()
        db.refresh(new_show)

        logger.info(f"Show created for ID: {new_show.id}")
        return ShowResponse.model_validate(new_show)

    except Exception as e:
        logger.error(f"Error creating show: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
