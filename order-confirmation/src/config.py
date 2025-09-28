from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "jdbc:postgresql://localhost:5433/postgres"
    REDIS_URL: str = "redis://localhost:6379/0"


settings = Settings() # type: ignore

broker_url = settings.REDIS_URL
result_backend = settings.REDIS_URL
