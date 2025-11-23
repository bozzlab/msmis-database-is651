from datetime import datetime

from pydantic import BaseModel


class CategoryCreateRequest(BaseModel):
    name: str
    user_id: int


class CategoryUpdateRequest(BaseModel):
    name: str
    user_id: int


class BaseCategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    last_modified_at: datetime

    class Config:
        orm_mode = True


class CategoryResponse(BaseModel):
    income: list[BaseCategoryResponse] = []
    expense: list[BaseCategoryResponse] = []

    class Config:
        orm_mode = True
