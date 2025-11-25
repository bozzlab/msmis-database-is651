from .base import CRUDBase
from app.models import models

from sqlalchemy.orm import Session, selectinload


class CRUDUser(CRUDBase):
    def get_by_condition(
        self,
        db: Session,
        username: str = None,
        email: str = None,
        id: int = None,
        include_options: bool = False,
    ) -> models.Users | None:
        filters = []
        options = []

        if include_options:
            options = [
                selectinload(models.Occupations),
                selectinload(models.PostalCodes),
                selectinload(models.WorkExperienceLevels),
                selectinload(models.Currencies),
                selectinload(models.EducationLevels),
            ]

        if username:
            filters.append(self.model.username == username)

        if id:
            filters.append(self.model.id == id)

        if email:
            filters.append(self.model.email == email)

        return db.query(self.model).filter(*filters).options(*options).first()


crud_user = CRUDUser(models.Users)
