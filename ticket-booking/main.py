from fastapi import FastAPI

from src.theaters.views import router as theater_router

app = FastAPI()
app.include_router(theater_router)


@app.get("/")
async def index():
    return {"message": "API is running"}
