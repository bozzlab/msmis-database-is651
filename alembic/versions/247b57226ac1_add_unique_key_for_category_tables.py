"""Add unique key for category tables

Revision ID: 247b57226ac1
Revises: 68e05569456c
Create Date: 2025-11-16 15:50:36.660395

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "247b57226ac1"
down_revision: Union[str, Sequence[str], None] = "68e05569456c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        "uq_expense_cat_user_name", "expense_categories", ["user_id", "name"]
    )
    op.create_unique_constraint(
        "uq_income_cat_user_name", "income_categories", ["user_id", "name"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_income_cat_user_name", "income_categories", type_="unique")
    op.drop_constraint("uq_expense_cat_user_name", "expense_categories", type_="unique")
