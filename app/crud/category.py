from .base import CRUDBase
from app.models import models


class CRUDCategory(CRUDBase):
    pass


crud_income_category = CRUDCategory(models.IncomeCategories)
crud_expense_category = CRUDCategory(models.ExpenseCategories)
