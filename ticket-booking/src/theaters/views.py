# required endpoints
# list theaters
# list theater by id

from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.theater import Theater
from ..logging import logger
from .models import TheaterResponse

router = APIRouter(prefix="/theaters")


@router.get("/")
async def get_theaters(db: DbSession) -> list[TheaterResponse]:
    try:
        theaters = db.query(Theater).all()
        if not theaters:
            logger.warning("No theaters found")
            raise HTTPException(status_code=404, detail="No theaters found")
        logger.info(f"Found {len(theaters)} theaters")
        return theaters

    except Exception as e:
        logger.error(f"Error listing theaters: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{theater_id}")
async def get_theaters_by_id(theater_id: UUID, db: DbSession) -> TheaterResponse:
    try:
        theater = db.query(Theater).filter(Theater.id == theater_id).first()
        logger.info(f"Found Theater for ID: {theater_id}")
        if not theater:
            logger.warning(f"No theaters found for ID {theater_id}")
            raise HTTPException(status_code=404, detail=f"No theater for ID: {theater_id}")
        return theater

        return theater
    except Exception as e:
        logger.error(f"Error listing theaters by ID: {theater_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
