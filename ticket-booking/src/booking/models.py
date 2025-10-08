from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class BookingResponse(BaseModel):
    id: UUID
    show_id: UUID
    seats_reserved: int
    booking_time: datetime


class BookingCreation(BaseModel):
    pass
