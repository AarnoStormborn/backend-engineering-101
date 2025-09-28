from fastapi import APIRouter
from .config import settings
from .models import ProductOrder

import time
import logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "API is running!"}


@router.post("/order/", response_model=ProductOrder)
async def place_order(order: ProductOrder):
    time.sleep(5)
    logging.info("Placing Order ...")
    return order
    

@router.get("/order_status/{order_id}")
async def get_order_status(order_id: int):
    pass

