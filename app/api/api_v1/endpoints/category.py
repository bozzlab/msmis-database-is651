from fastapi import Query, APIRouter, Depends, Body, HTTPException, status
from sqlalchemy.orm import Session

from pydantic import BaseModel

from app.api.dependency.db import get_db
from app.api.dependency.user import get_current_user
from app.schemas.category import (
    CategoryCreateRequest,
    CategoryResponse,
    CategorySummaryResponse,
)
from app.constants.category_type import CategoryType
from app.crud.category import crud_income_category, crud_expense_category
from app.services.category_service import CategoryService
from app.models import models

router = APIRouter(prefix="/categories", tags=["Category"])


def _validate_owner(
    current_user: models.Users, category_create: CategoryCreateRequest
) -> None:
    if current_user.id != category_create.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized for this category",
        )


@router.get("")
async def get_categories(
    db_session: Session = Depends(get_db),
    category_types: list[CategoryType] = Query(default=[*CategoryType]),
    current_user: models.Users = Depends(get_current_user),
) -> CategorySummaryResponse:
    service = CategoryService(db_session)
    categories = service.get_categories(
        user_id=current_user.id, category_types=category_types
    )

    return categories


@router.post("/income")
async def create_income_category(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    category_create: CategoryCreateRequest = Body(...),
) -> CategoryResponse:
    _validate_owner(current_user, category_create)

    return crud_income_category.create(db_session, obj_in=category_create)


@router.post("/expense")
async def create_expense_category(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    category_create: CategoryCreateRequest = Body(...),
) -> CategoryResponse:
    _validate_owner(current_user, category_create)

    return crud_expense_category.create(db_session, obj_in=category_create)


@router.put("/expense/{category_id}")
async def update_expense_category(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    category_id: int,
    category_name: str = Body(...),
) -> None:
    pass


@router.delete("/expense/{category_id}")
async def delete_expense_category(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    category_id: int,
) -> None:
    pass


@router.put("/income/{category_id}")
async def update_income_category(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    category_id: int,
    category_name: str = Body(...),
) -> None:
    pass


@router.delete("/income/{category_id}")
async def delete_income_category(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    category_id: int,
) -> None:
    pass
