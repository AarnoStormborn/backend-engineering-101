from fastapi import FastAPI
from src.orders import router

app = FastAPI()
app.include_router(router)
