import enum
import uuid

from sqlalchemy import Column, Enum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from ..core import Base


class Seat(Base):
    __tablename__ = "seats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    theater_id = Column(UUID(as_uuid=True), ForeignKey("theaters.id"), nullable=False)
    seat_num = Column(String, nullable=False)

    def __repr__(self):
        return f"<Seat(id={self.id}\tseat_num={self.seat_num})>"


class ShowSeatStatus(enum.Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    BOOKED = "booked"


class ShowSeat(Base):
    __tablename__ = "showseats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seat_id = Column(UUID(as_uuid=True), ForeignKey("seats.id"), nullable=False)
    show_id = Column(UUID(as_uuid=True), ForeignKey("shows.id"), nullable=False)
    status = Column(Enum(ShowSeatStatus), default=ShowSeatStatus.AVAILABLE)

    def __repr__(self):
        return f"<ShowSeat(id={self.id}\tstatus={self.status})>"
