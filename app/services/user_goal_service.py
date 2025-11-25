from datetime import datetime

from sqlalchemy import and_, text, func, case, select
from sqlalchemy.orm import Session

from app.constants.user_goal_type import UserGoalType
from app.constants.user_goal_status_type import UserGoalStatusType
from app.models.models import UserGoals, IncomeTransactions, ExpenseTransactions
from app.schemas.user_goal import GoalResponse, GoalSummaryResponse, GoalCreate
from app.crud.user_goal import crud_user_goal


class UserGoalService:
    def __init__(self, db_session: Session) -> None:
        self.db = db_session

    def create_goal(self, goal_create: GoalCreate) -> GoalResponse:
        status: UserGoalStatusType = None

        if goal_create.start_date > datetime.now().date():
            status = UserGoalStatusType.PENDING
        else:
            status = UserGoalStatusType.IN_PROGRESS

        goal_dict = goal_create.dict()
        goal_dict["status"] = status

        db_goal = UserGoals(**goal_dict)

        self.db.add(db_goal)
        self.db.commit()
        self.db.refresh(db_goal)

        return db_goal

    def get_goals(
        self,
        user_goal_types: list[UserGoalType],
        *,
        user_id: int,
        goal_id: int | None = None,
    ) -> list[GoalSummaryResponse]:
        income_sub = (
            select(func.coalesce(func.sum(IncomeTransactions.amount), 0))
            .where(IncomeTransactions.user_id == UserGoals.user_id)
            .where(IncomeTransactions.exclude_from_goal == False)
            .where(IncomeTransactions.transaction_datetime >= UserGoals.start_date)
            .where(
                IncomeTransactions.transaction_datetime
                < UserGoals.end_date + text("INTERVAL '1 day'")
            )
            .correlate(UserGoals)
            .scalar_subquery()
        )

        expense_sub = (
            select(func.coalesce(func.sum(ExpenseTransactions.amount), 0))
            .where(ExpenseTransactions.user_id == UserGoals.user_id)
            .where(ExpenseTransactions.exclude_from_goal == False)
            .where(ExpenseTransactions.transaction_datetime >= UserGoals.start_date)
            .where(
                ExpenseTransactions.transaction_datetime
                < UserGoals.end_date + text("INTERVAL '1 day'")
            )
            .correlate(UserGoals)
            .scalar_subquery()
        )

        progress_ratio = case(
            (UserGoals.amount == 0, 0),
            (
                UserGoals.target_goal == UserGoalType.LIMIT_EXPENSE,
                expense_sub / UserGoals.amount,
            ),
            (
                UserGoals.target_goal == UserGoalType.SAVING,
                (income_sub - expense_sub) / UserGoals.amount,
            ),
            else_=0,
        )

        calculated_status = case(
            (UserGoals.start_date > func.current_date(), UserGoalStatusType.PENDING),
            (func.current_date() <= UserGoals.end_date, UserGoalStatusType.IN_PROGRESS),
            else_=case(
                (
                    and_(
                        UserGoals.target_goal == UserGoalType.LIMIT_EXPENSE,
                        progress_ratio > 1,
                    ),
                    UserGoalStatusType.FAILED,
                ),
                (
                    and_(
                        UserGoals.target_goal == UserGoalType.LIMIT_EXPENSE,
                        progress_ratio <= 1,
                    ),
                    UserGoalStatusType.SUCCESS,
                ),
                (
                    and_(
                        UserGoals.target_goal == UserGoalType.SAVING,
                        progress_ratio >= 1,
                    ),
                    UserGoalStatusType.SUCCESS,
                ),
                else_=UserGoalStatusType.FAILED,
            ),
        )

        filters = [
            UserGoals.user_id == user_id,
            UserGoals.target_goal.in_(user_goal_types),
        ]

        if goal_id is not None:
            filters.append(UserGoals.id == goal_id)

        stmt = select(
            UserGoals,
            income_sub.label("total_income"),
            expense_sub.label("total_expense"),
            (progress_ratio * 100).label("progress"),
            calculated_status.label("status"),
        ).where(*filters)

        results = self.db.execute(stmt).all()

        processed_goals = []

        for row in results:
            goal_obj = row[0]
            goal_data = {
                "id": goal_obj.id,
                "name": goal_obj.name,
                "user_id": goal_obj.user_id,
                "target_goal": goal_obj.target_goal,
                "amount": goal_obj.amount,
                "start_date": goal_obj.start_date,
                "end_date": goal_obj.end_date,
                "total_income": row.total_income,
                "total_expense": row.total_expense,
                "progress": round(row.progress, 2) if row.progress else 0,
                "status": row.status,
            }

            processed_goals.append(GoalSummaryResponse(**goal_data))

        return processed_goals

    def update_goal_status(self, user_id: int) -> list[GoalSummaryResponse]:
        db_summary_goals = self.get_goals(
            user_goal_types=list(UserGoalType), user_id=user_id
        )

        for db_summary_goal in db_summary_goals:
            db_goal_to_update = crud_user_goal.get(self.db, id=db_summary_goal.id)

            if db_goal_to_update and db_goal_to_update.status != db_summary_goal.status:
                db_goal_to_update.status = db_summary_goal.status
                self.db.commit()
                self.db.refresh(db_goal_to_update)

        return self.get_goals(user_goal_types=list(UserGoalType), user_id=user_id)
