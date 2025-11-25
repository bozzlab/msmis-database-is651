from typing import Optional
from datetime import datetime

from fastapi import HTTPException, status

from pydantic import BaseModel, confloat, conint, validator
from .category import CategoryResponse
from .payment_method import PaymentMethod



class TransactionAttachment(BaseModel):
    id: int
    transaction_id: int
    filename: str
    file_type: str
    content_length_bytes: str
    path: str

    class Config:
        orm_mode = True


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


class TransactionCreate(BaseTransaction):
    pass


class TransactionUpdate(BaseModel):
    name: Optional[str] = None
    transaction_datetime: datetime = None
    amount: Optional[confloat(gt=0)] = None
    exclude_from_goal: Optional[bool] = None
    note: Optional[str] = None

    category_id: conint(ge=1) = None
    payment_method_id: conint(ge=1) = None

    @validator("transaction_datetime")
    def validate_transaction_datetime(cls, v) -> datetime:
        now = datetime.now()

        if v > now:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Transaction date cannot be in the future",
            )

        return v


class TransactionResponse(BaseTransaction):
    id: int

    category: CategoryResponse
    payment_method: PaymentMethod
    transaction_attachments: list[TransactionAttachment]

    class Config:
        orm_mode = True


class TransactionSummaryResponse(BaseModel):
    income: list[TransactionResponse] = []
    expense: list[TransactionResponse] = []

    class Config:
        orm_mode = True
