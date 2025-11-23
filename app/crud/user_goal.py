from .base import CRUDBase
from app.models import models


class CRUDUserGoal(CRUDBase):
    pass


crud_user_goal = CRUDUserGoal(models.UserGoals)
