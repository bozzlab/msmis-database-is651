from fastapi import HTTPException, Query, status, Depends, APIRouter, Body
from app.api.dependency.db import get_db

from app.models import models
from app.constants.transaction_type import TransactionType
from app.constants.transaction_preset_range_type import TransactionPresetRangeType
from app.schemas.transaction import (
    BaseTransactionCreate,
    TransactionResponse,
    BaseTransactionResponse,
)
from sqlalchemy.orm import Session
from app.crud.transaction import crud_income_transaction, crud_expense_transaction
from app.services.transaction_service import TransactionService
from app.api.dependency.user import get_current_user


router = APIRouter(prefix="/transactions", tags=["Transactions"])


def _validate_owner(current_user: models.Users, transaction_create: BaseTransactionCreate) -> None:
    if current_user.id != transaction_create.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create transaction for this user",
        )

@router.get("")
async def get_transactions(
    db_session: Session = Depends(get_db),
    transaction_types: list[TransactionType] = Query(default=[*TransactionType]),
    transaction_preset_range_type: TransactionPresetRangeType = Query(
        default=TransactionPresetRangeType.TODAY
    ),
    current_user: models.Users = Depends(get_current_user),
) -> TransactionResponse:
    service = TransactionService(db_session)
    transactions = service.get_transactions(
        transaction_types=transaction_types,
        preset_range=transaction_preset_range_type,
        user_id=current_user.id,
    )

    return transactions


@router.post("/income")
async def create_income_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    transaction_create: BaseTransactionCreate = Body(...),
) -> BaseTransactionResponse:
    _validate_owner(current_user, transaction_create)

    return crud_income_transaction.create(db_session, obj_in=transaction_create)


@router.post("/expense")
async def create_expense_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    transaction_create: BaseTransactionCreate = Body(...),
) -> BaseTransactionResponse:
    _validate_owner(current_user, transaction_create)

    return crud_expense_transaction.create(db_session, obj_in=transaction_create)


@router.put("/expense/{transaction_id}")
async def update_expense_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
    transaction_name: str = Body(...),
) -> dict:
    pass


@router.delete("/expense/{transaction_id}")
async def delete_expense_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
) -> dict:
    pass


@router.put("/income/{transaction_id}")
async def update_income_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
    transaction_name: str = Body(...),
) -> dict:
    pass


@router.delete("/income/{transaction_id}")
async def delete_income_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
) -> dict:
    pass
