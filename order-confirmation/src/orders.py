from fastapi import APIRouter, HTTPException

from .models import OrderCreate, OrderResponse
from .tasks import confirm_order
from .db.core import DbSession
from .db.entities import Order

import logging
logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "API is running!"}


@router.post("/order/", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: DbSession):
    try:
        logging.info("Placing Order ...")
        
        new_order = Order(**order.model_dump())
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        
        confirm_order.delay(new_order.id)
        
        print(new_order)
        
        logging.info(f"Order placed\tOrder ID: {new_order.id}")
        return OrderResponse.model_validate(new_order)
    
    except Exception as e:
        logging.error(f"Something went wrong: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    


@router.get("/orders/", response_model=list[OrderResponse])
async def get_orders(db: DbSession):
    orders = db.query(Order).all()
    if not orders:
        raise HTTPException(status_code=404, detail="Orders Not found")
    return orders


@router.get("/orders/{order_id}", response_model=OrderResponse)
async def get_order_by_id(order_id: int, db: DbSession):
    order = db.query(Order).filter(Order.id == order_id).first() # type: ignore
    if not order:
        raise HTTPException(status_code=404, detail=f"Order not found for ID {order_id}")
    return order
    
    

