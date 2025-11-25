from datetime import datetime, timedelta
from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.constants.transaction_type import TransactionType
from app.constants.transaction_preset_range_type import TransactionPresetRangeType
from app.models.models import IncomeTransactions, ExpenseTransactions
from app.schemas.transaction import TransactionResponse, TransactionSummaryResponse


TRANSACTION_TYPE_MODEL_MAP = {
    TransactionType.INCOME: IncomeTransactions,
    TransactionType.EXPENSE: ExpenseTransactions,
}

ATTACHMENT_TRANSACTION_TYPE_MODEL_MAP = {
    TransactionType.INCOME: "income_transaction_attachments",
    TransactionType.EXPENSE: "expense_transaction_attachments",
}


class TransactionService:
    def __init__(self, db_session: Session) -> None:
        self.db = db_session

    def get_transactions(
        self,
        user_id: int,
        transaction_types: list[TransactionType] = list(TransactionType),
        preset_range: TransactionPresetRangeType = TransactionPresetRangeType.TODAY,
    ) -> TransactionSummaryResponse:
        response = TransactionSummaryResponse(income=[], expense=[])

        for transaction_type in transaction_types:
            model = TRANSACTION_TYPE_MODEL_MAP.get(transaction_type)
            db_transactions = (
                self.db.query(model)
                .filter(
                    model.user_id == user_id,
                    self._get_preset_range_filter(model, preset_range),
                )
                .options(
                    [
                        selectinload(model.payment_method),
                        selectinload(model.category),
                        selectinload(model.transaction_attachments),
                    ]
                )
                .all()
            )

            if db_transactions:
                for db_transaction in db_transactions:
                    setattr(
                        response,
                        transaction_type.value.lower(),
                        [
                            TransactionResponse.from_orm(db_category)
                            for db_category in db_transactions
                        ],
                    )

        return response

    def _get_preset_range_filter(
        self, model, preset_range: TransactionPresetRangeType
    ) -> any:
        now = datetime.now()

        present_map = {
            TransactionPresetRangeType.TODAY: and_(
                model.transaction_datetime >= datetime(now.year, now.month, now.day),
                model.transaction_datetime
                < datetime(now.year, now.month, now.day) + timedelta(days=1),
            ),
            TransactionPresetRangeType.WEEKLY: and_(
                model.transaction_datetime
                >= datetime.combine(
                    now - timedelta(days=now.weekday()), datetime.min.time()
                ),
                model.transaction_datetime
                < datetime.combine(
                    now - timedelta(days=now.weekday()), datetime.min.time()
                )
                + timedelta(days=7),
            ),
            TransactionPresetRangeType.MONTHLY: and_(
                model.transaction_datetime >= datetime(now.year, now.month, 1),
                model.transaction_datetime
                < datetime(now.year + int(now.month / 12), (now.month % 12) + 1, 1),
            ),
            TransactionPresetRangeType.QUARTERLY: and_(
                model.transaction_datetime
                >= (
                    datetime(now.year - 1, now.month + 10, 1)
                    if now.month <= 2
                    else datetime(now.year, now.month - 2, 1)
                ),
                model.transaction_datetime
                < datetime(now.year + int(now.month / 12), (now.month % 12) + 1, 1),
            ),
            TransactionPresetRangeType.YEARLY: and_(
                model.transaction_datetime >= datetime(now.year, 1, 1),
                model.transaction_datetime < datetime(now.year + 1, 1, 1),
            ),
        }

        if preset_range not in present_map:
            raise ValueError(f"Invalid period: {preset_range}")

        return present_map[preset_range]
