from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BookingResponse(BaseModel):
    id: UUID
    show_id: UUID
    seats_reserved: int
    booking_time: datetime

    model_config = ConfigDict(from_attributes=True)


class BookingCreation(BaseModel):
    show_id: UUID
    seats_reserved: int
    booking_time: datetime
