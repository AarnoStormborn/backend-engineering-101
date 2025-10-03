import uuid
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

from ..core import Base

class Show(Base):
    
    __tablename__ = "shows"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    theater_id = Column(UUID(as_uuid=True), ForeignKey('theaters.id'), nullable=False)
    movie_id = Column(UUID(as_uuid=True), ForeignKey('movies.id'), nullable=False)
    show_time = Column(DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("Asia/Kolkata")))
    price = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<Show(id={self.id}, show_time={self.show_time})>"
    


