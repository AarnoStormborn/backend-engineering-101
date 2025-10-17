# endpoints needed

# create booking
# list bookings
# list available seats for a booking


from fastapi import APIRouter, HTTPException

from ..db.core import DbSession
from ..db.entities.booking import Booking
from ..logging import logger
from .models import BookingCreate, BookingResponse

router = APIRouter(prefix="/bookings")


@router.post("/create")
async def create_booking(booking: BookingCreate, db: DbSession):
    try:
        logger.info(f"Data received: {booking.model_dump()}")

        new_booking = Booking(**booking.model_dump())
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)

        logger.info(f"Booking created with ID: {new_booking.id}")

        return BookingResponse.model_validate(new_booking)
    except Exception as e:
        logger.error(f"Error creating Booking: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
