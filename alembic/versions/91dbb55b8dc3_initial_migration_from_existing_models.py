"""Initial migration from existing models

Revision ID: 91dbb55b8dc3
Revises:
Create Date: 2025-11-03 22:43:18.037949

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "91dbb55b8dc3"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "currencies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(length=10), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column(
            "active", sa.Boolean(), server_default=sa.text("true"), nullable=True
        ),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="currencies_pkey"),
        sa.UniqueConstraint("code", name="currencies_code_key"),
    )
    op.create_table(
        "education_levels",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("level", sa.String(length=255), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="education_levels_pkey"),
    )
    op.create_table(
        "expense_payment_methods",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column(
            "is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False
        ),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="expense_payment_methods_pkey"),
    )
    op.create_table(
        "income_payment_methods",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column(
            "is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False
        ),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="income_payment_methods_pkey"),
    )
    op.create_table(
        "notification_types",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column(
            "delivery_channel",
            sa.Enum("EMAIL", "APP_PUSH", "SMS", name="notification_type_channel_enum"),
            nullable=False,
        ),
        sa.Column("template_title", sa.String(length=255), nullable=False),
        sa.Column("template_body", sa.Text(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="notification_types_pkey"),
        sa.UniqueConstraint("name", name="notification_types_name_key"),
    )
    op.create_table(
        "occupations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="occupations_pkey"),
    )
    op.create_table(
        "partners",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column(
            "is_active", sa.Boolean(), server_default=sa.text("true"), nullable=True
        ),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="partners_pkey"),
        sa.UniqueConstraint("name", name="partners_name_key"),
    )
    op.create_table(
        "postal_codes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("postal_code", sa.String(length=20), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="postal_codes_pkey"),
        sa.UniqueConstraint("postal_code", name="postal_codes_postal_code_key"),
    )
    op.create_table(
        "subscription_plans",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column(
            "billing_cycle",
            sa.Enum("MONTHLY", "YEARLY", name="subscription_plan_billing_cycle"),
            nullable=False,
        ),
        sa.Column(
            "is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False
        ),
        sa.Column("features", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.CheckConstraint(
            "price >= 0::numeric", name="subscription_plans_price_check"
        ),
        sa.PrimaryKeyConstraint("id", name="subscription_plans_pkey"),
        sa.UniqueConstraint("name", name="subscription_plans_name_key"),
    )
    op.create_table(
        "work_experience_levels",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("level", sa.String(length=255), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="work_experience_levels_pkey"),
    )
    op.create_table(
        "partner_products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("partner_id", sa.Integer(), nullable=False),
        sa.Column("type", sa.String(length=100), nullable=True),
        sa.Column("remark", sa.Text(), nullable=True),
        sa.Column(
            "is_active", sa.Boolean(), server_default=sa.text("true"), nullable=True
        ),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["partner_id"], ["partners.id"], name="fk_partner_prod_partner"
        ),
        sa.PrimaryKeyConstraint("id", name="partner_products_pkey"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("phone_number", sa.String(length=50), nullable=False),
        sa.Column("first_name", sa.String(length=100), nullable=False),
        sa.Column("last_name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("dob", sa.Date(), nullable=False),
        sa.Column(
            "gender",
            sa.Enum("F", "M", "Others", "Rather not to say", name="gender_enum"),
            nullable=False,
        ),
        sa.Column("occupation_id", sa.Integer(), nullable=False),
        sa.Column("work_experience_level_id", sa.Integer(), nullable=False),
        sa.Column("education_level_id", sa.Integer(), nullable=False),
        sa.Column("postal_code_id", sa.Integer(), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("personal_data_consent", sa.Boolean(), nullable=False),
        sa.Column("marketing_consent", sa.Boolean(), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "age",
            sa.Integer(),
            sa.Computed(
                "CAST( (2025 - EXTRACT(YEAR FROM dob)) AS INTEGER)", persisted=True
            ),
            nullable=False,
            comment="[WARNING] Hardcoded age calculation based on year 2025.",
        ),
        sa.ForeignKeyConstraint(
            ["currency_id"], ["currencies.id"], name="fk_users_currency"
        ),
        sa.ForeignKeyConstraint(
            ["education_level_id"], ["education_levels.id"], name="fk_users_edu_level"
        ),
        sa.ForeignKeyConstraint(
            ["occupation_id"], ["occupations.id"], name="fk_users_occupation"
        ),
        sa.ForeignKeyConstraint(
            ["postal_code_id"], ["postal_codes.id"], name="fk_users_postal_code"
        ),
        sa.ForeignKeyConstraint(
            ["work_experience_level_id"],
            ["work_experience_levels.id"],
            name="fk_users_work_exp",
        ),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.UniqueConstraint("email", name="users_email_key"),
        sa.UniqueConstraint("phone_number", name="users_phone_number_key"),
        sa.UniqueConstraint("username", name="users_username_key"),
    )
    op.create_table(
        "expense_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_exp_cat_user"),
        sa.PrimaryKeyConstraint("id", name="expense_categories_pkey"),
    )
    op.create_table(
        "income_categories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_income_cat_user"),
        sa.PrimaryKeyConstraint("id", name="income_categories_pkey"),
    )
    op.create_table(
        "user_goals",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "target_goal",
            sa.Enum("LIMIT EXPENSE", "SAVING", name="goal_target_enum"),
            nullable=False,
        ),
        sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("start_date", sa.Date(), nullable=False),
        sa.Column("end_date", sa.Date(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "IN_PROGRESS", "FAILED", "PENDING", "SUCCESS", name="goal_status_enum"
            ),
            nullable=False,
        ),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_goals_user"),
        sa.PrimaryKeyConstraint("id", name="user_goals_pkey"),
    )
    op.create_table(
        "user_notifications",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("type_id", sa.Integer(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "PENDING",
                "SENT",
                "READ",
                "FAILED",
                name="user_notification_status_enum",
            ),
            server_default=sa.text("'PENDING'::user_notification_status_enum"),
            nullable=False,
        ),
        sa.Column(
            "scheduled_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("sent_at", sa.DateTime(), nullable=True),
        sa.Column("read_at", sa.DateTime(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["type_id"],
            ["notification_types.id"],
            name="user_notifications_type_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="user_notifications_user_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="user_notifications_pkey"),
    )
    op.create_table(
        "user_partner_products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("partner_product_id", sa.Integer(), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["partner_product_id"], ["partner_products.id"], name="fk_user_partner_prod"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_partner_user"),
        sa.PrimaryKeyConstraint("id", name="user_partner_products_pkey"),
        sa.UniqueConstraint(
            "user_id",
            "partner_product_id",
            name="user_partner_products_user_id_partner_product_id_key",
        ),
    )
    op.create_table(
        "user_subscriptions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("plan_id", sa.Integer(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "ACTIVE",
                "CANCELLED",
                "TRIAL",
                "PAST_DUE",
                "EXPIRED",
                name="user_subscriptions_status",
            ),
            nullable=False,
        ),
        sa.Column(
            "renews_automatically",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column("last_payment_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("next_billing_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_sub_user"),
        sa.PrimaryKeyConstraint("id", name="user_subscriptions_pkey"),
        sa.UniqueConstraint("user_id", name="user_subscriptions_user_id_key"),
    )
    op.create_table(
        "expense_planned_transactions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column(
            "amount",
            sa.Numeric(precision=10, scale=2),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column(
            "interval",
            sa.Enum(
                "WEEKLY",
                "MONTHLY",
                "BI_WEEKLY",
                "QUARTERLY",
                "HALF_YEAR",
                "YEARLY",
                name="expense_interval_enum",
            ),
            nullable=False,
        ),
        sa.Column("start_date", sa.Date(), nullable=True),
        sa.Column("end_date", sa.Date(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["category_id"], ["expense_categories.id"], name="fk_exp_plan_cat"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_exp_plan_user"),
        sa.PrimaryKeyConstraint("id", name="expense_planned_transactions_pkey"),
    )
    op.create_table(
        "expense_transactions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("transaction_datetime", sa.DateTime(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column(
            "exclude_from_goal",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=True,
        ),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("payment_method_id", sa.Integer(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.CheckConstraint(
            "amount > 0::numeric", name="expense_transactions_amount_check"
        ),
        sa.ForeignKeyConstraint(
            ["category_id"], ["expense_categories.id"], name="fk_exp_trans_cat"
        ),
        sa.ForeignKeyConstraint(
            ["currency_id"], ["currencies.id"], name="fk_exp_trans_currency"
        ),
        sa.ForeignKeyConstraint(
            ["payment_method_id"],
            ["expense_payment_methods.id"],
            name="fk_exp_trans_payment",
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_exp_trans_user"),
        sa.PrimaryKeyConstraint("id", name="expense_transactions_pkey"),
    )
    op.create_table(
        "income_planned_transactions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column(
            "interval",
            sa.Enum(
                "WEEKLY",
                "MONTHLY",
                "BI_WEEKLY",
                "QUARTERLY",
                "HALF_YEAR",
                "YEARLY",
                name="income_interval_enum",
            ),
            nullable=False,
        ),
        sa.Column("start_date", sa.Date(), nullable=True),
        sa.Column("end_date", sa.Date(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["category_id"], ["income_categories.id"], name="fk_income_plan_cat"
        ),
        sa.ForeignKeyConstraint(
            ["currency_id"], ["currencies.id"], name="fk_income_plan_currency"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_income_plan_user"),
        sa.PrimaryKeyConstraint("id", name="income_planned_transactions_pkey"),
    )
    op.create_table(
        "income_transactions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("transaction_date", sa.DateTime(), nullable=False),
        sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column(
            "exclude_from_goal",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=True,
        ),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("payment_method_id", sa.Integer(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.CheckConstraint(
            "amount > 0::numeric", name="income_transactions_amount_check"
        ),
        sa.ForeignKeyConstraint(
            ["category_id"], ["income_categories.id"], name="fk_income_trans_cat"
        ),
        sa.ForeignKeyConstraint(
            ["currency_id"], ["currencies.id"], name="fk_income_trans_currency"
        ),
        sa.ForeignKeyConstraint(
            ["payment_method_id"],
            ["income_payment_methods.id"],
            name="fk_income_trans_payment",
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_income_trans_user"),
        sa.PrimaryKeyConstraint("id", name="income_transactions_pkey"),
    )
    op.create_table(
        "expense_planned_transaction_occurences",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("plan_id", sa.Integer(), nullable=False),
        sa.Column(
            "amount",
            sa.Numeric(precision=10, scale=2),
            server_default=sa.text("0"),
            nullable=False,
        ),
        sa.Column("paid_date", sa.Date(), nullable=False),
        sa.Column("transaction_id", sa.Integer(), nullable=True),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["plan_id"], ["expense_planned_transactions.id"], name="fk_exp_occur_plan"
        ),
        sa.ForeignKeyConstraint(
            ["transaction_id"],
            ["expense_transactions.id"],
            name="fk_exp_occur_trans",
            ondelete="SET NULL",
        ),
        sa.PrimaryKeyConstraint(
            "id", name="expense_planned_transaction_occurences_pkey"
        ),
    )
    op.create_table(
        "expense_transaction_attachments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("transaction_id", sa.Integer(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column(
            "file_type",
            sa.Enum("jpg", "png", "pdf", name="file_type_enum"),
            nullable=False,
        ),
        sa.Column("content_length_bytes", sa.BigInteger(), nullable=False),
        sa.Column("path", sa.String(length=1024), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.CheckConstraint(
            "content_length_bytes < 10485760",
            name="expense_transaction_attachments_content_length_bytes_check",
        ),
        sa.ForeignKeyConstraint(
            ["transaction_id"], ["expense_transactions.id"], name="fk_exp_attach_trans"
        ),
        sa.PrimaryKeyConstraint("id", name="expense_transaction_attachments_pkey"),
    )
    op.create_table(
        "income_transaction_attachments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("transaction_id", sa.Integer(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column("path", sa.String(length=1024), nullable=False),
        sa.Column(
            "last_modified_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["transaction_id"],
            ["income_transactions.id"],
            name="fk_income_attach_trans",
        ),
        sa.PrimaryKeyConstraint("id", name="income_transaction_attachments_pkey"),
    )

    # trigger

    op.execute("""               
    CREATE OR REPLACE FUNCTION update_last_modified_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.last_modified_at = NOW();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """)

    op.execute("""
            CREATE TRIGGER set_timestamp_occupations BEFORE UPDATE ON occupations FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_work_experience_levels BEFORE UPDATE ON work_experience_levels FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_postal_codes BEFORE UPDATE ON postal_codes FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_education_levels BEFORE UPDATE ON education_levels FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_currencies BEFORE UPDATE ON currencies FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_partners BEFORE UPDATE ON partners FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_partner_products BEFORE UPDATE ON partner_products FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_users BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_user_subscriptions BEFORE UPDATE ON user_subscriptions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_user_goals BEFORE UPDATE ON user_goals FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_user_partner_products BEFORE UPDATE ON user_partner_products FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_income_payment_methods BEFORE UPDATE ON income_payment_methods FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_income_categories BEFORE UPDATE ON income_categories FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_income_transactions BEFORE UPDATE ON income_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_income_transaction_attachments BEFORE UPDATE ON income_transaction_attachments FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_income_planned_transactions BEFORE UPDATE ON income_planned_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_expense_payment_methods BEFORE UPDATE ON expense_payment_methods FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_expense_categories BEFORE UPDATE ON expense_categories FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_expense_transactions BEFORE UPDATE ON expense_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_expense_transaction_attachments BEFORE UPDATE ON expense_transaction_attachments FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_expense_planned_transactions BEFORE UPDATE ON expense_planned_transactions FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_expense_planned_transaction_occurences BEFORE UPDATE ON expense_planned_transaction_occurences FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_subscription_plans BEFORE UPDATE ON subscription_plans FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_notification_types BEFORE UPDATE ON notification_types FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();
            CREATE TRIGGER set_timestamp_user_notifications BEFORE UPDATE ON user_notifications FOR EACH ROW EXECUTE FUNCTION update_last_modified_at_column();               
    """)

    # Reference data

    op.execute("""
        INSERT INTO occupations (name) VALUES 
        ('Accountant'),
        ('Administrative Assistant'),
        ('Advertising Executive'),
        ('Agribusiness Manager'),
        ('Airline Pilot'),
        ('Architect'),
        ('Auditor'),
        ('Automotive Technician'),
        ('Barista'),
        ('Biotechnologist'),
        ('Brand Manager'),
        ('Business Development Manager'),
        ('Carpenter'),
        ('Chef'),
        ('Construction Foreman'),
        ('Content Creator'),
        ('Cybersecurity Specialist'),
        ('Data Analyst'),
        ('Data Scientist'),
        ('Dentist'),
        ('Digital Marketing Specialist'),
        ('Diving Instructor'),
        ('Doctor'),
        ('E-commerce Specialist'),
        ('Economist'),
        ('Engineer'),
        ('Financial Analyst'),
        ('Fitness Trainer'),
        ('Food Scientist'),
        ('Foreign Language Translator'),
        ('Freelance'),
        ('Government Officer'),
        ('Graphic Designer'),
        ('Hotel Manager'),
        ('HR Manager'),
        ('Insurance Agent'),
        ('Investment Banker'),
        ('Lawyer'),
        ('Jewelry Craftsman'),
        ('Journalist / Reporter'),
        ('Legal Counsel / Corporate Lawyer'),
        ('Librarian'),
        ('Logistics Coordinator'),
        ('Medical Specialist'),
        ('Model'),
        ('Nurse'),
        ('Pharmacist'),
        ('Plumber'),
        ('Police Officer'),
        ('Project Manager'),
        ('Psychologist'),
        ('Real Estate Agent'),
        ('Receptionist'),
        ('Sales'),
        ('Software Developer'),
        ('Taxi Driver'),
        ('Teacher'),
        ('Tour Guide'),
        ('UX/UI Designer'),
        ('Veterinarian');
    """)

    op.execute("""
    INSERT INTO work_experience_levels (level) VALUES
        ('New grad'),
        ('0-2 years'),
        ('3-5 years'),
        ('6-10 years'),
        ('11-15 years'),
        ('16-20 years'),
        ('21-25 years'),
        ('26-30 years'),
        ('over 30 years');               
    """)

    op.execute("""
        INSERT INTO postal_codes (postal_code) VALUES 
        ('10100'),
        ('10110'),
        ('10120'),
        ('10130'),
        ('10140'),
        ('10150'),
        ('10160'),
        ('10170'),
        ('10200'),
        ('10210'),
        ('10220'),
        ('10230'),
        ('10240'),
        ('10250'),
        ('10260'),
        ('10300'),
        ('10310'),
        ('10320'),
        ('10330'),
        ('10400'),
        ('10500'),
        ('10510'),
        ('10520'),
        ('10530'),
        ('10540'),
        ('11000'),
        ('11110'),
        ('11120'),
        ('11130'),
        ('11140'),
        ('11150'),
        ('12000'),
        ('12110'),
        ('12120'),
        ('12130'),
        ('12140'),
        ('12150'),
        ('13000'),
        ('13110'),
        ('13120'),
        ('13130'),
        ('13140'),
        ('14000'),
        ('14110'),
        ('14120'),
        ('14130'),
        ('14140'),
        ('15000'),
        ('15110'),
        ('15120'),
        ('15130'),
        ('15140'),
        ('16000'),
        ('16110'),
        ('16120'),
        ('16130'),
        ('16140'),
        ('17000'),
        ('17110'),
        ('17120'),
        ('17130'),
        ('17140'),
        ('18000'),
        ('18110'),
        ('18120'),
        ('18130'),
        ('18140'),
        ('19000'),
        ('19110'),
        ('19120'),
        ('19130'),
        ('19140'),
        ('20000'),
        ('20110'),
        ('20120'),
        ('20130'),
        ('20140'),
        ('21000'),
        ('21110'),
        ('21120'),
        ('21130'),
        ('21140'),
        ('22000'),
        ('22110'),
        ('22120'),
        ('22130'),
        ('22140'),
        ('23000'),
        ('23110'),
        ('23120'),
        ('23130'),
        ('23140'),
        ('24000'),
        ('24110'),
        ('24120'),
        ('24130'),
        ('24140'),
        ('25000'),
        ('25110'),
        ('25120'),
        ('25130'),
        ('25140'),
        ('26000'),
        ('26110'),
        ('26120'),
        ('26130'),
        ('26140'),
        ('27000'),
        ('27110'),
        ('27120'),
        ('27130'),
        ('27140'),
        ('30000'),
        ('30110'),
        ('30120'),
        ('30130'),
        ('30140'),
        ('31000'),
        ('31110'),
        ('31120'),
        ('31130'),
        ('31140'),
        ('32000'),
        ('32110'),
        ('32120'),
        ('32130'),
        ('32140'),
        ('33000'),
        ('33110'),
        ('33120'),
        ('33130'),
        ('33140'),
        ('34000'),
        ('34110'),
        ('34120'),
        ('34130'),
        ('34140'),
        ('35000'),
        ('35110'),
        ('35120'),
        ('35130'),
        ('35140'),
        ('36000'),
        ('36110'),
        ('36120'),
        ('36130'),
        ('36140'),
        ('37000'),
        ('37110'),
        ('37120'),
        ('37130'),
        ('37140'),
        ('38000'),
        ('38110'),
        ('38120'),
        ('38130'),
        ('38140'),
        ('39000'),
        ('39110'),
        ('39120'),
        ('39130'),
        ('39140'),
        ('40000'),
        ('40110'),
        ('40120'),
        ('40130'),
        ('40140'),
        ('41000'),
        ('41110'),
        ('41120'),
        ('41130'),
        ('41140'),
        ('42000'),
        ('42110'),
        ('42120'),
        ('42130'),
        ('42140'),
        ('43000'),
        ('43110'),
        ('43120'),
        ('43130'),
        ('43140'),
        ('44000'),
        ('44110'),
        ('44120'),
        ('44130'),
        ('44140'),
        ('45000'),
        ('45110'),
        ('45120'),
        ('45130'),
        ('45140'),
        ('46000'),
        ('46110'),
        ('46120'),
        ('46130'),
        ('46140'),
        ('47000'),
        ('47110'),
        ('47120'),
        ('47130'),
        ('47140'),
        ('48000'),
        ('48110'),
        ('48120'),
        ('48130'),
        ('48140'),
        ('49000'),
        ('49110'),
        ('49120'),
        ('49130'),
        ('49140'),
        ('50000'),
        ('50110'),
        ('50120'),
        ('50130'),
        ('50140'),
        ('51000'),
        ('51110'),
        ('51120'),
        ('51130'),
        ('51140'),
        ('52000'),
        ('52110'),
        ('52120'),
        ('52130'),
        ('52140'),
        ('53000'),
        ('53110'),
        ('53120'),
        ('53130'),
        ('53140'),
        ('54000'),
        ('54110'),
        ('54120'),
        ('54130'),
        ('54140'),
        ('55000'),
        ('55110'),
        ('55120'),
        ('55130'),
        ('55140'),
        ('56000'),
        ('56110'),
        ('56120'),
        ('56130'),
        ('56140'),
        ('57000'),
        ('57110'),
        ('57120'),
        ('57130'),
        ('57140'),
        ('58000'),
        ('58110'),
        ('58120'),
        ('58130'),
        ('58140'),
        ('60000'),
        ('60110'),
        ('60120'),
        ('60130'),
        ('60140'),
        ('61000'),
        ('61110'),
        ('61120'),
        ('61130'),
        ('61140'),
        ('62000'),
        ('62110'),
        ('62120'),
        ('62130'),
        ('62140'),
        ('63000'),
        ('63110'),
        ('63120'),
        ('63130'),
        ('63140'),
        ('64000'),
        ('64110'),
        ('64120'),
        ('64130'),
        ('64140'),
        ('65000'),
        ('65110'),
        ('65120'),
        ('65130'),
        ('65140'),
        ('66000'),
        ('66110'),
        ('66120'),
        ('66130'),
        ('66140'),
        ('67000'),
        ('67110'),
        ('67120'),
        ('67130'),
        ('67140'),
        ('70000'),
        ('70110'),
        ('70120'),
        ('70130'),
        ('70140'),
        ('71000'),
        ('71110'),
        ('71120'),
        ('71130'),
        ('71140'),
        ('72000'),
        ('72110'),
        ('72120'),
        ('72130'),
        ('72140'),
        ('73000'),
        ('73110'),
        ('73120'),
        ('73130'),
        ('73140'),
        ('74000'),
        ('74110'),
        ('74120'),
        ('74130'),
        ('74140'),
        ('75000'),
        ('75110'),
        ('75120'),
        ('75130'),
        ('75140'),
        ('76000'),
        ('76110'),
        ('76120'),
        ('76130'),
        ('76140'),
        ('77000'),
        ('77110'),
        ('77120'),
        ('77130'),
        ('77140'),
        ('80000'),
        ('80110'),
        ('80120'),
        ('80130'),
        ('80140'),
        ('81000'),
        ('81110'),
        ('81120'),
        ('81130'),
        ('81140'),
        ('82000'),
        ('82110'),
        ('82120'),
        ('82130'),
        ('82140'),
        ('83000'),
        ('83110'),
        ('83120'),
        ('83130'),
        ('83140'),
        ('84000'),
        ('84110'),
        ('84120'),
        ('84130'),
        ('84140'),
        ('85000'),
        ('85110'),
        ('85120'),
        ('85130'),
        ('85140'),
        ('86000'),
        ('86110'),
        ('86120'),
        ('86130'),
        ('86140'),
        ('90000'),
        ('90110'),
        ('90120'),
        ('90130'),
        ('90140'),
        ('91000'),
        ('91110'),
        ('91120'),
        ('91130'),
        ('91140'),
        ('92000'),
        ('92110'),
        ('92120'),
        ('92130'),
        ('92140'),
        ('93000'),
        ('93110'),
        ('93120'),
        ('93130'),
        ('93140'),
        ('94000'),
        ('94110'),
        ('94120'),
        ('94130'),
        ('94140'),
        ('95000'),
        ('95110'),
        ('95120'),
        ('95130'),
        ('95140'),
        ('96000'),
        ('96110'),
        ('96120'),
        ('96130'),
        ('96140');               
    """)

    op.execute("""
    INSERT INTO education_levels (level) VALUES 
    ('High School Diploma'),
    ('Vocational Certificate'),
    ('Technical College'),
    ('Bachelor Degree'),
    ('Master Degree'),
    ('Doctor Degrees');
    """)

    op.execute("""
    INSERT INTO currencies (code) VALUES 
        ('THB'),
        ('USD'),
        ('EUR'),
        ('JPY'),
        ('GBP'),
        ('AUD'),
        ('CAD'),
        ('CHF'),
        ('CNY'),
        ('HKD'),
        ('SGD'),
        ('NZD'),
        ('KRW'),
        ('INR'),
        ('MYR');
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("income_transaction_attachments")
    op.drop_table("expense_transaction_attachments")
    op.drop_table("expense_planned_transaction_occurences")
    op.drop_table("income_transactions")
    op.drop_table("income_planned_transactions")
    op.drop_table("expense_transactions")
    op.drop_table("expense_planned_transactions")
    op.drop_table("user_subscriptions")
    op.drop_table("user_partner_products")
    op.drop_table("user_notifications")
    op.drop_table("user_goals")
    op.drop_table("income_categories")
    op.drop_table("expense_categories")
    op.drop_table("users")
    op.drop_table("partner_products")
    op.drop_table("work_experience_levels")
    op.drop_table("subscription_plans")
    op.drop_table("postal_codes")
    op.drop_table("partners")
    op.drop_table("occupations")
    op.drop_table("notification_types")
    op.drop_table("income_payment_methods")
    op.drop_table("expense_payment_methods")
    op.drop_table("education_levels")
    op.drop_table("currencies")

    # drop trigger and function

    op.execute("""               
        DROP TYPE IF EXISTS
            gender_enum,
            subscription_tier_enum,
            subscription_plan_billing_cycle,
            user_subscriptions_status,
            user_notification_status_enum,
            notification_type_channel_enum,
            goal_target_enum,
            goal_status_enum,
            income_interval_enum,
            file_type_enum,
            expense_interval_enum
        CASCADE;
    """)

    op.execute("DROP FUNCTION IF EXISTS update_last_modified_at_column() CASCADE;")
