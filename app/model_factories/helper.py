import random
from sqlalchemy.sql.expression import func
from typing import Type, TypeVar

T = TypeVar("T")


def get_random_existing(model_class: Type[T]) -> T:
    from .base import BaseFactory

    session = BaseFactory._meta.sqlalchemy_session

    if not session:
        raise Exception(
            "Session not injected into BaseFactory._meta.sqlalchemy_session"
        )

    record = session.query(model_class).order_by(func.random()).first()

    if not record:
        raise Exception(
            f"No existing records found for {model_class.__name__}. "
            "Did you run the seed script first?"
        )

    return record
