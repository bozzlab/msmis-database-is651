from .base import CRUDBase
from app.models import models

from sqlalchemy.orm import Session


class CRUDUser(CRUDBase):
    def get_by_condition(
        self, db: Session, username: str = None, email: str = None
    ) -> models.Users | None:
        filters = []

        if username:
            filters.append(self.model.username == username)

        if email:
            filters.append(self.model.email == email)

        return db.query(self.model).filter(*filters).first()


crud_user = CRUDUser(models.Users)
