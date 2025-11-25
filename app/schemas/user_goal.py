from __future__ import annotations

from datetime import date, datetime

from fastapi import HTTPException, status

from pydantic import BaseModel, conint, Field, confloat, root_validator

from app.constants.user_goal_type import UserGoalType
from app.constants.user_goal_status_type import UserGoalStatusType


class GoalCreate(BaseModel):
    user_id: conint(ge=1)
    name: str = Field(..., max_length=255)
    target_goal: UserGoalType
    amount: confloat(gt=0)
    start_date: date
    end_date: date

    @root_validator
    def validate_dates(cls, values) -> GoalCreate:
        start_date = values.get("start_date")
        end_date = values.get("end_date")

        if start_date > end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Start date must be before or equal to end date.",
            )

        if end_date < datetime.now().date():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Cannot create goal end date in the past",
            )

        return values


class GoalUpdate(BaseModel):
    name: str = Field(..., max_length=255)
    target_goal: UserGoalType
    amount: confloat(gt=0)
    start_date: date
    end_date: date


class GoalResponse(BaseModel):
    user_id: conint(ge=1)
    name: str = Field(..., max_length=255)
    target_goal: UserGoalType
    amount: confloat(gt=0)
    start_date: date
    end_date: date
    id: conint(ge=1)
    status: UserGoalStatusType

    class Config:
        orm_mode = True


class GoalSummaryResponse(GoalResponse):
    total_income: float
    total_expense: float
    progress: float
