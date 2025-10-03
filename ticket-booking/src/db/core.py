from typing import Annotated

from ..logging import logger
from ..config import settings

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session


engine = create_engine(url=settings.DATABASE_URL)
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
)
Base = declarative_base()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
        
DbSession = Annotated[Session, Depends(get_db)]
