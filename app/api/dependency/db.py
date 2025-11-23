import logging

from sqlalchemy.exc import DBAPIError

from app.db.session import db_session


LOGGER = logging.getLogger("DBLogger")


def get_db():
    try:
        db = db_session()
        yield db
    except DBAPIError as db_api_error:
        LOGGER.error(db_api_error)
        db.rollback()
        raise
    finally:
        db.close()
