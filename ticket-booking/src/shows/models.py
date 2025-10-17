from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ShowResponse(BaseModel):
    id: UUID
    theater_id: UUID
    movie_id: UUID
    show_time: datetime
    price: int

    model_config = ConfigDict(from_attributes=True)


class ShowCreate(BaseModel):
    theater_id: UUID
    movie_id: UUID
    show_time: datetime
    price: int
