from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MovieResponse(BaseModel):
    id: UUID
    name: str
    runtime: int
    released_on: date

    model_config = ConfigDict(from_attributes=True)


class MovieCreate(BaseModel):
    name: str
    runtime: int
    released_on: date
