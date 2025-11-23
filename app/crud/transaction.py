from .base import CRUDBase
from app.models import models


class CRUDTransactions(CRUDBase):
    pass


crud_income_transaction = CRUDTransactions(models.IncomeTransactions)
crud_expense_transaction = CRUDTransactions(models.ExpenseTransactions)
