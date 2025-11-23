from fastapi import HTTPException, status, Depends
from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.models import models
from app.api.dependency.db import get_db
from .auth import get_access_token


def validate_user_creation(db_session: Session, user_create: UserCreate) -> UserCreate:
    stmt = select(models.Users).where(
        or_(
            models.Users.username == user_create.username,
            models.Users.email == user_create.email,
            models.Users.phone_number == user_create.phone_number,
        )
    )

    existing_user = db_session.scalar(stmt)

    if existing_user:
        if existing_user.username == user_create.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )
        if existing_user.email == user_create.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
            )
        if existing_user.phone_number == user_create.phone_number:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Phone number already exists",
            )

    return user_create


def get_current_user(
    user_id: int = Depends(get_access_token), db: Session = Depends(get_db)
) -> models.Users:
    user = db.query(models.Users).filter(models.Users.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user
