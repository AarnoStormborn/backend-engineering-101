from fastapi import APIRouter

from .config import settings
from .models import OrderCreate
from .db.core import DbSession
from .db.entities import Order

import time
import logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "API is running!"}


@router.post("/order/", response_model=OrderCreate)
async def place_order(order: OrderCreate, db: DbSession):
    time.sleep(1)
    logging.info("Placing Order ...")
    
    new_order = Order(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    logging.info(f"Order placed\tOrder ID: {new_order.id}")
    
    return order
    

@router.get("/order_status/{order_id}")
async def get_order_status(order_id: int):
    pass

