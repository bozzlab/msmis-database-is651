import calendar
import random
from datetime import datetime
from typing import Type, TypeVar

from sqlalchemy.sql.expression import func

T = TypeVar("T")


def get_random_existing(
    model_class: Type[T], user_id: int | None = None, **custom_filters
) -> T:
    from .base import BaseFactory

    session = BaseFactory._meta.sqlalchemy_session

    if not session:
        raise Exception(
            "Session not injected into BaseFactory._meta.sqlalchemy_session"
        )

    filters = []

    if user_id:
        filters.append(model_class.user_id == user_id)

    if custom_filters:
        for attr, value in custom_filters.items():
            if value == "IS_NOT_NONE":
                filters.append(getattr(model_class, attr) != None)
            else:
                filters.append(getattr(model_class, attr) == value)

    record = session.query(model_class).filter(*filters).order_by(func.random()).first()

    if not record:
        raise Exception(
            f"No existing records found for {model_class.__name__}. "
            "Did you run the seed script first?"
        )

    return record


def generate_mock_dates(
    start_year: int = 2024,
    end_year: int = 2025,
    end_month: int = 11,
    min_per_month: int = 1,
    max_per_month: int = 31,
) -> list[datetime]:
    date_ranges = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == end_year and month > end_month:
                break

            _, days_in_month = calendar.monthrange(year, month)

            real_max_count = min(max_per_month, days_in_month)

            real_min_count = min(min_per_month, real_max_count)

            count = random.randint(real_min_count, real_max_count)

            for day in random.sample(range(1, days_in_month + 1), count):
                dt = datetime(
                    year, month, day, random.randint(8, 22), random.randint(0, 59)
                )
                date_ranges.append(dt)

    date_ranges.sort()

    return date_ranges
