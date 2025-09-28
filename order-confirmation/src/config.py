import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str | None = os.getenv("DATABASE_URL")
    REDIS_URL: str | None = os.getenv("REDIS_URL")


settings = Settings() # type: ignore

# broker_url = settings.REDIS_URL
# result_backend = settings.REDIS_URL
