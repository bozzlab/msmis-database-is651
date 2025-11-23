from app.db.session import db_session
from contextlib import contextmanager


from model_factories.base import BaseFactory


@contextmanager
def factory_session_scope() -> None:
    print("... [Factory Session] Injecting session into BaseFactory ...")
    BaseFactory._meta.sqlalchemy_session = db_session

    try:
        yield db_session

    finally:
        print("... [Factory Session] Tearing down session ...")
        db_session.remove()

        BaseFactory._meta.sqlalchemy_session = None
