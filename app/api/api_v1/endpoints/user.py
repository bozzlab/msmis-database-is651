from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session

from app.api.dependency.db import get_db
from app.api.dependency.user import get_current_user, validate_user_creation
from app.crud.user import crud_user
from app.schemas.user import UserCreate, UserResponse, UserUpdate, UserStatus, UserLogin
from app.utils import encode_util
from app.models import models

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(db_session=Depends(get_db), *, user_id: int) -> UserResponse:
    db_user = crud_user.get_by_condition(db_session, id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return db_user


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(
    db_session=Depends(get_db), *, user_create: UserCreate
) -> UserResponse:
    validated_user = validate_user_creation(db_session, user_create=user_create)
    db_user = crud_user.create(db_session, obj_in=validated_user)

    return crud_user.get_by_condition(db_session, id=db_user.id)


@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(db_session=Depends(get_db), *, user_update: UserUpdate):
    pass


@router.patch("/users/{user_id}/status", status_code=status.HTTP_200_OK)
async def update_user_status(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    user_id: int,
    user_status: UserStatus,
) -> UserResponse:
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this user's status",
        )

    db_user = crud_user.get(db_session, id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    db_user = crud_user.update(db_session, id=db_user.id, obj_in=user_status)

    return db_user


@router.post("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_access_token(db_session=Depends(get_db), *, user_login: UserLogin) -> str:
    db_user = crud_user.get_by_condition(db_session, username=user_login.username)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if db_user.password_hash != user_login.password_hash:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return encode_util.encode_base64(db_user.id)
