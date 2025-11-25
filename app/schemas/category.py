from datetime import datetime

from pydantic import BaseModel


class CategoryCreateRequest(BaseModel):
    name: str
    user_id: int


class CategoryUpdateRequest(BaseModel):
    name: str
    user_id: int


class CategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    last_modified_at: datetime

    class Config:
        orm_mode = True


class CategorySummaryResponse(BaseModel):
    income: list[CategoryResponse] = []
    expense: list[CategoryResponse] = []

    class Config:
        orm_mode = True
