from fastapi import HTTPException, Query, status, Depends, APIRouter, Body
from app.api.dependency.db import get_db

from app.models import models
from app.constants.transaction_type import TransactionType
from app.constants.transaction_preset_range_type import TransactionPresetRangeType
from app.schemas.transaction import (
    TransactionCreate,
    TransactionSummaryResponse,
    TransactionResponse,
    TransactionUpdate,
)
from sqlalchemy.orm import Session
from app.crud.transaction import crud_income_transaction, crud_expense_transaction
from app.services.transaction_service import TransactionService
from app.api.dependency.user import get_current_user


router = APIRouter(prefix="/transactions", tags=["Transactions"])


def _validate_owner(
    current_user: models.Users, transaction_create: TransactionCreate
) -> None:
    if current_user.id != transaction_create.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized for this transaction",
        )


@router.get("")
async def get_transactions(
    db_session: Session = Depends(get_db),
    transaction_types: list[TransactionType] = Query(default=[*TransactionType]),
    transaction_preset_range_type: TransactionPresetRangeType = Query(
        default=TransactionPresetRangeType.TODAY
    ),
    current_user: models.Users = Depends(get_current_user),
) -> TransactionSummaryResponse:
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
    transaction_create: TransactionCreate = Body(...),
) -> TransactionResponse:
    _validate_owner(current_user, transaction_create)

    return crud_income_transaction.create(db_session, obj_in=transaction_create)


@router.post("/expense")
async def create_expense_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    transaction_create: TransactionCreate = Body(...),
) -> TransactionResponse:
    _validate_owner(current_user, transaction_create)

    return crud_expense_transaction.create(db_session, obj_in=transaction_create)


@router.put("/expense/{transaction_id}")
async def update_expense_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
    transaction_update: TransactionUpdate = Body(...),
):
    db_transaction = crud_expense_transaction.get(db=db_session, id=transaction_id)

    if not db_transaction:
        raise HTTPException(status_code=404, detail="not found transaction")

    _validate_owner(current_user, db_transaction)
    
    tx_id = db_transaction.id

    crud_expense_transaction.update(db=db_session, id=tx_id, obj_in=transaction_update)

    return crud_expense_transaction.get_by_condition(db_session=db_session, id=tx_id)


@router.delete("/expense/{transaction_id}", status_code=204)
async def delete_expense_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,

) -> None:
    db_transaction = crud_expense_transaction.get(db=db_session, id=transaction_id)

    if not db_transaction:
        raise HTTPException(status_code=404, detail="not found transaction")

    _validate_owner(current_user, db_transaction)
    
    crud_expense_transaction.delete(db_session, db_transaction.id)


@router.put("/income/{transaction_id}")
async def update_income_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
    transaction_update: TransactionUpdate = Body(...),
) -> dict:
    db_transaction = crud_income_transaction.get(db=db_session, id=transaction_id)

    if not db_transaction:
        raise HTTPException(status_code=404, detail="not found transaction")

    _validate_owner(current_user, db_transaction)
    
    tx_id = db_transaction.id

    crud_income_transaction.update(db=db_session, id=tx_id, obj_in=transaction_update)

    return crud_income_transaction.get_by_condition(db_session=db_session, id=tx_id)


@router.delete("/income/{transaction_id}")
async def delete_income_transaction(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    transaction_id: int,
) -> dict:
    db_transaction = crud_expense_transaction.get(db=db_session, id=transaction_id)

    if not db_transaction:
        raise HTTPException(status_code=404, detail="not found transaction")

    _validate_owner(current_user, db_transaction)
    
    crud_income_transaction.delete(db_session, db_transaction.id)
