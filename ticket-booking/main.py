from fastapi import FastAPI

from src.movies.views import router as movie_router
from src.theaters.views import router as theater_router

app = FastAPI()
app.include_router(theater_router)
app.include_router(movie_router)


# @app.on_event("startup")
# async def on_startup():
#     init_db()
#     logger.info("Database tables created")


@app.get("/")
async def index():
    return {"message": "API is running"}
