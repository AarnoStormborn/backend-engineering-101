import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from ..core import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    runtime = Column(Integer, nullable=False)
    released_on = Column(Date, nullable=False, default=lambda: datetime.now(ZoneInfo("Asia/Kolkata")))

    def __repr__(self):
        return f"<Movie(id={self.id}\tname={self.name})>"
