from sqlalchemy.orm import selectinload, Session

from .base import CRUDBase
from app.models import models



class CRUDTransactions(CRUDBase):
    def get_by_condition(self, db_session: Session, *, id: int | None = None, user_id: int | None = None) -> models.Base:
        filters = []

        if id: 
            filters.append(self.model.id == id)

        if user_id: 
            filters.append(self.model.user_id == user_id)

        return  (
                        db_session.query(self.model)
                        .filter(*filters)
                        .options(
                            [
                                selectinload(self.model.payment_method),
                                selectinload(self.model.category),
                                selectinload(self.model.transaction_attachments),
                            ]
                        )
                        .all()
                    )


crud_income_transaction = CRUDTransactions(models.IncomeTransactions)
crud_expense_transaction = CRUDTransactions(models.ExpenseTransactions)
