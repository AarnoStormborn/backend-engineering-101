import uuid
from datetime import datetime, timezone 
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.dialects.postgresql import UUID

from zoneinfo import ZoneInfo

from ..core import Base


class Movie(Base):
    
    __tablename__ = "movies"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    runtime = Column(Integer, nullable=False)
    released_on = Column(Date, nullable=False, default=lambda: datetime.now(ZoneInfo("Asia/Kolkata")))
    
    def __repr__(self):
        return f"<Movie(id={self.id}\tname={self.name})>"