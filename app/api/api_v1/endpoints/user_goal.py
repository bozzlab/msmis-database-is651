from fastapi import HTTPException, Query, status, Depends, APIRouter, Body
from app.api.dependency.db import get_db

from app.models import models
from app.constants.user_goal_status_type import UserGoalStatusType
from app.constants.user_goal_type import UserGoalType
from app.schemas.user_goal import (
    GoalCreate,
    GoalSummaryResponse,
    GoalUpdate,
    GoalResponse,
)
from sqlalchemy.orm import Session
from app.crud.user_goal import crud_user_goal
from app.services.user_goal_service import UserGoalService
from app.api.dependency.user import get_current_user


router = APIRouter(prefix="/user_goals", tags=["User Goals"])


def _validate_owner(current_user: models.Users, goal_create: GoalCreate) -> None:
    if current_user.id != goal_create.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create goal for this user",
        )


@router.get("")
async def get_goals(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    user_goal_types: list[UserGoalType] = Query(default=[*UserGoalType]),
    goal_id: int | None = Query(default=None, ge=1),
) -> list[GoalSummaryResponse]:
    service = UserGoalService(db_session)
    goals = service.get_goals(
        user_goal_types=user_goal_types, user_id=current_user.id, goal_id=goal_id
    )

    return goals


@router.post("")
async def create_user_goal(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    goal_create: GoalCreate = Body(...),
) -> GoalResponse:
    _validate_owner(current_user, goal_create)
    service = UserGoalService(db_session)

    return service.create_goal(goal_create=goal_create)


@router.patch("/{user_goal_id}/status")
async def update_goal_status(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    user_goal_id: int,
) -> None:
    if current_user.id != user_goal_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update goal for this user",
        )


@router.put("/{user_goal_id}")
async def update_goal(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    user_goal_id: int,
    goal_update: GoalUpdate,
) -> None:
    if current_user.id != user_goal_id.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update goal for this user",
        )


@router.delete("/{user_goal_id}")
async def delete_goal(
    db_session: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
    *,
    user_goal_id: int,
) -> None:
    if current_user.id != user_goal_id.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update goal for this user",
        )
