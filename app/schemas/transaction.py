from typing import Optional
from datetime import datetime

from fastapi import HTTPException, status

from pydantic import BaseModel, confloat, conint, validator


class BaseTransaction(BaseModel):
    transaction_datetime: datetime
    name: str
    amount: confloat(gt=0)
    exclude_from_goal: Optional[bool] = False
    note: Optional[str] = None

    user_id: conint(ge=1)
    category_id: conint(ge=1)
    payment_method_id: conint(ge=1)

    @validator("transaction_datetime")
    def validate_transaction_datetime(cls, v) -> datetime:
        now = datetime.now()

        if v > now:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Transaction date cannot be in the future",
            )

        return v


class BaseTransactionCreate(BaseTransaction):
    pass


class TransactionUpdate(BaseModel):
    name: Optional[str] = None
    transaction_datetime: datetime
    amount: Optional[confloat(gt=0)] = None
    exclude_from_goal: Optional[bool] = None
    note: Optional[str] = None

    category_id: conint(ge=1)
    payment_method_id: conint(ge=1)

    @validator("transaction_datetime")
    def validate_transaction_datetime(cls, v) -> datetime:
        now = datetime.now()

        if v > now:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Transaction date cannot be in the future",
            )

        return v


class BaseTransactionResponse(BaseTransaction):
    id: int

    class Config:
        orm_mode = True


class TransactionResponse(BaseModel):
    income: list[BaseTransactionResponse] = []
    expense: list[BaseTransactionResponse] = []

    class Config:
        orm_mode = True
