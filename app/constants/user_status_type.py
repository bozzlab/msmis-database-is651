from enum import Enum


class UserStatusType(str, Enum):
    ACTIVATED = "ACTIVATED"
    INACTIVATED = "INACTIVATED"
    PENDING = "PENDING"
