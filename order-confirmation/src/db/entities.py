from .core import Base
from sqlalchemy import Column, String, Integer, Enum

import enum

class OrderStatus(enum.Enum):
    SUCCESS = "success"
    PENDING = "pending"
    FAILED = "failed"

class Order(Base):
    
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)
    
    def __repr__(self):
        return f"<Order(id={self.id}, name={self.name})>"
    
    