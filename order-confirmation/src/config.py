import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str 
    REDIS_URL: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings() # type: ignore

broker_url = settings.REDIS_URL
result_backend = settings.REDIS_URL
