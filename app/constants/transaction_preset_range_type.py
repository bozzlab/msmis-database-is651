from enum import Enum


class TransactionPresetRangeType(str, Enum):
    TODAY = "today"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"
