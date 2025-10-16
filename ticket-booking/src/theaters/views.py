# required endpoints
# list theaters
# list theater by id

from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.theater import Theater
from ..logging import logger
from .models import TheaterCreate, TheaterResponse

router = APIRouter(prefix="/theaters")


@router.get("/")
async def get_theaters(db: DbSession) -> list[TheaterResponse]:
    theaters = db.query(Theater).all()
    if not theaters:
        logger.warning("No theaters found")
        raise HTTPException(status_code=404, detail="No theaters found")
    logger.info(f"Found {len(theaters)} theaters")
    return theaters


@router.get("/{theater_id}")
async def get_theaters_by_id(theater_id: UUID, db: DbSession) -> TheaterResponse:
    theater = db.query(Theater).filter(Theater.id == theater_id).first()
    if not theater:
        raise HTTPException(status_code=404, detail=f"No theater for ID: {theater_id}")
    logger.info(f"Found Theater for ID: {theater_id}")
    return theater


@router.post("/create")
async def create_theater(theater: TheaterCreate, db: DbSession):
    try:
        logger.info(f"Data received: {theater.model_dump()}")
        new_theater = Theater(**theater.model_dump())
        db.add(new_theater)
        db.commit()
        db.refresh(new_theater)

        logger.info(f"Creating theater with ID: {new_theater.id}")

        return TheaterResponse.model_validate(new_theater)

    except Exception as e:
        logger.error("Error creating theater")
        raise HTTPException(status_code=500, detail=str(e))
