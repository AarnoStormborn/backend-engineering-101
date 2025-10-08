from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from ..config import settings

engine = create_engine(url=settings.DATABASE_URL)
LocalSession = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


DbSession = Annotated[Session, Depends(get_db)]
