
import uuid
from sqlalchemy import Column, String, Date, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID

from ..core import Base

class Theater(Base):
    
    __tablename__ = "theaters"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False) 
    
    def __repr__(self):
        return f"<Theater(id={self.id}\tname={self.name})>"
    