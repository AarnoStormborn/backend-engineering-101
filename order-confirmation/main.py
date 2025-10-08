from fastapi import FastAPI

from src.db.core import Base, engine
from src.orders import router

Base.metadata.create_all(bind=engine)  # type: ignore

app = FastAPI()
app.include_router(router)
