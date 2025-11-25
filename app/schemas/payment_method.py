from datetime import datetime

from pydantic import BaseModel


class PaymentMethod(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True
