# required endpoints
# list theaters
# list theater by id


from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.theater import Theater

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "API is running"}


@router.get("/theaters/")
async def get_theaters(db: DbSession):
    try:
        movies = db.query(Theater).all()
        if not movies:
            raise HTTPException(detail="No theaters found")

    except Exception:
        pass
