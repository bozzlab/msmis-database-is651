from enum import Enum


class UserGoalStatusType(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
