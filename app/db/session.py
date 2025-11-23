from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core.settings import get_settings


engine = create_engine(str(get_settings().DATABASE_URI), pool_pre_ping=True, echo=False)
session_factory = sessionmaker(bind=engine)
db_session = scoped_session(session_factory)
