from typing import Annotated
from ..config import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import Depends

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
DbSession = Annotated[Session, Depends(get_db)]
        