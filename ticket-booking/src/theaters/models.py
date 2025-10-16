from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TheaterResponse(BaseModel):
    id: UUID
    name: str

    model_config = ConfigDict(from_attributes=True)


class TheaterCreate(BaseModel):
    name: str
