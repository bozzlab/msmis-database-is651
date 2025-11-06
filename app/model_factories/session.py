# app/factory/session.py
from contextlib import contextmanager  # <--- 1. Import ตัวนี้
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core.settings import get_settings
from app.model_factories.base import BaseFactory

engine = create_engine(str(get_settings().DATABASE_URI), pool_pre_ping=True, echo=False)
session_factory = sessionmaker(bind=engine)


@contextmanager
def factory_session_scope():
    db_session = scoped_session(session_factory)

    print("... [Factory Session] Injecting session into BaseFactory ...")
    BaseFactory._meta.sqlalchemy_session = db_session

    try:
        yield db_session

    finally:
        print("... [Factory Session] Tearing down session ...")
        db_session.remove()

        BaseFactory._meta.sqlalchemy_session = None
