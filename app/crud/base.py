from typing import Type, Optional
from sqlalchemy.orm import Session

from app.models.models import Base


class CRUDBase:
    def __init__(self, model: Type[Base]):
        self.model = model

    def get(self, db: Session, id: int) -> Optional[Base]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> list[Base]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: Base) -> Base:
        db_obj = self.model(**obj_in.dict())

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def update(self, db: Session, id: int, obj_in: Base) -> Optional[Base]:
        obj_in: dict = obj_in.dict(exclude_unset=True)

        db_obj = db.query(self.model).filter(self.model.id == id).first()
        
        if db_obj:
            for key, value in obj_in.items():
                setattr(db_obj, key, value)
        
            db.commit()
            db.refresh(db_obj)
        
        return db_obj

    def delete(self, db: Session, id: int) -> Optional[Base]:
        db_obj = db.query(self.model).filter(self.model.id == id).first()

        if db_obj:
            db.delete(db_obj)
            db.commit()
        
        return db_obj
