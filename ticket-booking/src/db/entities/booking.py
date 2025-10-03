
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from ..core import Base

class Booking(Base):
    
    __tablename__ = "bookings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    show_id = Column(UUID(as_uuid=True), ForeignKey('shows.id'), nullable=False)
    seats_reserved = Column(Integer, nullable=False)
    booking_time = Column(DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("Asia/Kolkata")))

    def __repr__(self):
        return f"<Booking(id={self.id})>"
    
    
class BookingSeat(Base):
    
    __tablename__ = "bookingseats"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_id = Column(UUID(as_uuid=True), ForeignKey('bookings.id'), nullable=False)
    show_seat_id = Column(UUID(as_uuid=True), ForeignKey('showseats.id'), nullable=False)

