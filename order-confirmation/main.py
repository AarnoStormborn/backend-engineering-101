from fastapi import FastAPI
from src.orders import router

from src.db.core import Base, engine
from src.db.entities import Order

Base.metadata.create_all(bind=engine) # type: ignore

app = FastAPI()
app.include_router(router)
