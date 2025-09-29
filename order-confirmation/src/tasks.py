
import time

from celery import Celery
from sqlalchemy.orm import Session

from .db.core import SessionLocal
from .db.entities import Order, OrderStatus

import logging
logging.basicConfig(level="INFO")

celery_app = Celery()
celery_app.config_from_object('src.config')


@celery_app.task()
def confirm_order(order_id: int):
    
    try:
        print("CELERY TASK STARTED")
        db = SessionLocal()
    
        logging.info(f"Confirming order number {order_id} ... ")
        time.sleep(20)
        
        order_pending = db.query(Order).filter(Order.id == order_id).first()
        order_pending.status = OrderStatus.SUCCESS # type: ignore
        db.commit()
        logging.info("Order Confirmed !!")
        
    except Exception as e:
        print(str(e))
        logging.error(f"Celery Problem: {str(e)}")
        
    finally:
        db.close()