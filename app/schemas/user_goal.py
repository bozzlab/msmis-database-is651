from __future__ import annotations

from datetime import date

from fastapi import HTTPException, status

from pydantic import BaseModel, conint, Field, confloat, root_validator

from app.constants.user_goal_type import UserGoalType
from app.constants.user_goal_status_type import UserGoalStatusType


class BaseGoalCreate(BaseModel):
    user_id: conint(ge=1)
    name: str = Field(..., max_length=255)
    target_goal: UserGoalType
    amount: confloat(gt=0)
    start_date: date
    end_date: date
    status: UserGoalStatusType = UserGoalStatusType.PENDING

    @root_validator
    def validate_dates(cls, values) -> BaseGoalCreate:
        start_date = values.get("start_date")
        end_date = values.get("end_date")

        if start_date > end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Start date must be before or equal to end date.",
            )

        return values


class BaseGoalUpdate(BaseModel):
    status: UserGoalStatusType


class BaseGoalResponse(BaseGoalCreate):
    id: conint(ge=1)
    status: UserGoalStatusType

    class Config:
        orm_mode = True


class GoalResponse(BaseGoalResponse):
    total_income: float
    total_expense: float
    progress: float

