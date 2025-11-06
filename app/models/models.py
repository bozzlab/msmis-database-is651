from typing import Optional
import datetime
import decimal

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    Enum,
    ForeignKeyConstraint,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
    Text,
    UniqueConstraint,
    text,
    Computed,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Currencies(Base):
    __tablename__ = "currencies"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="currencies_pkey"),
        UniqueConstraint("code", name="currencies_code_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text("true"))
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    users: Mapped[list["Users"]] = relationship("Users", back_populates="currency")


class EducationLevels(Base):
    __tablename__ = "education_levels"
    __table_args__ = (PrimaryKeyConstraint("id", name="education_levels_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level: Mapped[Optional[str]] = mapped_column(String(255))
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    users: Mapped[list["Users"]] = relationship(
        "Users", back_populates="education_level"
    )


class ExpensePaymentMethods(Base):
    __tablename__ = "expense_payment_methods"
    __table_args__ = (PrimaryKeyConstraint("id", name="expense_payment_methods_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    expense_transactions: Mapped[list["ExpenseTransactions"]] = relationship(
        "ExpenseTransactions", back_populates="payment_method"
    )


class IncomePaymentMethods(Base):
    __tablename__ = "income_payment_methods"
    __table_args__ = (PrimaryKeyConstraint("id", name="income_payment_methods_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    income_transactions: Mapped[list["IncomeTransactions"]] = relationship(
        "IncomeTransactions", back_populates="payment_method"
    )


class NotificationTypes(Base):
    __tablename__ = "notification_types"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="notification_types_pkey"),
        UniqueConstraint("name", name="notification_types_name_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    delivery_channel: Mapped[str] = mapped_column(
        Enum("EMAIL", "APP_PUSH", "SMS", name="notification_type_channel_enum"),
        nullable=False,
    )
    template_title: Mapped[str] = mapped_column(String(255), nullable=False)
    template_body: Mapped[Optional[str]] = mapped_column(Text)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    user_notifications: Mapped[list["UserNotifications"]] = relationship(
        "UserNotifications", back_populates="type"
    )


class Occupations(Base):
    __tablename__ = "occupations"
    __table_args__ = (PrimaryKeyConstraint("id", name="occupations_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    users: Mapped[list["Users"]] = relationship("Users", back_populates="occupation")


class Partners(Base):
    __tablename__ = "partners"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="partners_pkey"),
        UniqueConstraint("name", name="partners_name_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(
        Boolean, server_default=text("true")
    )
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    partner_products: Mapped[list["PartnerProducts"]] = relationship(
        "PartnerProducts", back_populates="partner"
    )


class PostalCodes(Base):
    __tablename__ = "postal_codes"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="postal_codes_pkey"),
        UniqueConstraint("postal_code", name="postal_codes_postal_code_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    postal_code: Mapped[str] = mapped_column(String(20), nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    users: Mapped[list["Users"]] = relationship("Users", back_populates="postal_code")


class SubscriptionPlans(Base):
    __tablename__ = "subscription_plans"
    __table_args__ = (
        CheckConstraint("price >= 0::numeric", name="subscription_plans_price_check"),
        PrimaryKeyConstraint("id", name="subscription_plans_pkey"),
        UniqueConstraint("name", name="subscription_plans_name_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    billing_cycle: Mapped[str] = mapped_column(
        Enum("MONTHLY", "YEARLY", name="subscription_plan_billing_cycle"),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )
    features: Mapped[Optional[dict]] = mapped_column(JSONB)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )


class WorkExperienceLevels(Base):
    __tablename__ = "work_experience_levels"
    __table_args__ = (PrimaryKeyConstraint("id", name="work_experience_levels_pkey"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level: Mapped[Optional[str]] = mapped_column(String(255))
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    users: Mapped[list["Users"]] = relationship(
        "Users", back_populates="work_experience_level"
    )


class PartnerProducts(Base):
    __tablename__ = "partner_products"
    __table_args__ = (
        ForeignKeyConstraint(
            ["partner_id"], ["partners.id"], name="fk_partner_prod_partner"
        ),
        PrimaryKeyConstraint("id", name="partner_products_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    partner_id: Mapped[int] = mapped_column(Integer, nullable=False)
    type: Mapped[Optional[str]] = mapped_column(String(100))
    remark: Mapped[Optional[str]] = mapped_column(Text)
    is_active: Mapped[Optional[bool]] = mapped_column(
        Boolean, server_default=text("true")
    )
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    partner: Mapped["Partners"] = relationship(
        "Partners", back_populates="partner_products"
    )
    user_partner_products: Mapped[list["UserPartnerProducts"]] = relationship(
        "UserPartnerProducts", back_populates="partner_product"
    )


class Users(Base):
    __tablename__ = "users"
    __table_args__ = (
        ForeignKeyConstraint(
            ["currency_id"], ["currencies.id"], name="fk_users_currency"
        ),
        ForeignKeyConstraint(
            ["education_level_id"], ["education_levels.id"], name="fk_users_edu_level"
        ),
        ForeignKeyConstraint(
            ["occupation_id"], ["occupations.id"], name="fk_users_occupation"
        ),
        ForeignKeyConstraint(
            ["postal_code_id"], ["postal_codes.id"], name="fk_users_postal_code"
        ),
        ForeignKeyConstraint(
            ["work_experience_level_id"],
            ["work_experience_levels.id"],
            name="fk_users_work_exp",
        ),
        PrimaryKeyConstraint("id", name="users_pkey"),
        UniqueConstraint("email", name="users_email_key"),
        UniqueConstraint("phone_number", name="users_phone_number_key"),
        UniqueConstraint("username", name="users_username_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    dob: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    gender: Mapped[str] = mapped_column(
        Enum("F", "M", "Others", "Rather not to say", name="gender_enum"),
        nullable=False,
    )
    occupation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    work_experience_level_id: Mapped[int] = mapped_column(Integer, nullable=False)
    education_level_id: Mapped[int] = mapped_column(Integer, nullable=False)
    postal_code_id: Mapped[int] = mapped_column(Integer, nullable=False)
    currency_id: Mapped[int] = mapped_column(Integer, nullable=False)
    personal_data_consent: Mapped[bool] = mapped_column(Boolean, nullable=False)
    marketing_consent: Mapped[bool] = mapped_column(Boolean, nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    age: Mapped[int] = mapped_column(
        Integer,
        Computed("CAST( (2025 - EXTRACT(YEAR FROM dob)) AS INTEGER)", persisted=True),
        nullable=False,
        comment="Calculated user age based on 'dob' (GENERATED ALWAYS AS ... STORED)",
    )
    currency: Mapped["Currencies"] = relationship("Currencies", back_populates="users")
    education_level: Mapped["EducationLevels"] = relationship(
        "EducationLevels", back_populates="users"
    )
    occupation: Mapped["Occupations"] = relationship(
        "Occupations", back_populates="users"
    )
    postal_code: Mapped["PostalCodes"] = relationship(
        "PostalCodes", back_populates="users"
    )
    work_experience_level: Mapped["WorkExperienceLevels"] = relationship(
        "WorkExperienceLevels", back_populates="users"
    )
    expense_categories: Mapped[list["ExpenseCategories"]] = relationship(
        "ExpenseCategories", back_populates="user"
    )
    income_categories: Mapped[list["IncomeCategories"]] = relationship(
        "IncomeCategories", back_populates="user"
    )
    user_goals: Mapped[list["UserGoals"]] = relationship(
        "UserGoals", back_populates="user"
    )
    user_notifications: Mapped[list["UserNotifications"]] = relationship(
        "UserNotifications", back_populates="user"
    )
    user_partner_products: Mapped[list["UserPartnerProducts"]] = relationship(
        "UserPartnerProducts", back_populates="user"
    )
    user_subscriptions: Mapped["UserSubscriptions"] = relationship(
        "UserSubscriptions", uselist=False, back_populates="user"
    )
    expense_planned_transactions: Mapped[list["ExpensePlannedTransactions"]] = (
        relationship("ExpensePlannedTransactions", back_populates="user")
    )
    expense_transactions: Mapped[list["ExpenseTransactions"]] = relationship(
        "ExpenseTransactions", back_populates="user"
    )
    income_planned_transactions: Mapped[list["IncomePlannedTransactions"]] = (
        relationship("IncomePlannedTransactions", back_populates="user")
    )
    income_transactions: Mapped[list["IncomeTransactions"]] = relationship(
        "IncomeTransactions", back_populates="user"
    )


class ExpenseCategories(Base):
    __tablename__ = "expense_categories"
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_exp_cat_user"),
        PrimaryKeyConstraint("id", name="expense_categories_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    user: Mapped["Users"] = relationship("Users", back_populates="expense_categories")
    expense_planned_transactions: Mapped[list["ExpensePlannedTransactions"]] = (
        relationship("ExpensePlannedTransactions", back_populates="category")
    )
    expense_transactions: Mapped[list["ExpenseTransactions"]] = relationship(
        "ExpenseTransactions", back_populates="category"
    )


class IncomeCategories(Base):
    __tablename__ = "income_categories"
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_income_cat_user"),
        PrimaryKeyConstraint("id", name="income_categories_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    user: Mapped["Users"] = relationship("Users", back_populates="income_categories")
    income_planned_transactions: Mapped[list["IncomePlannedTransactions"]] = (
        relationship("IncomePlannedTransactions", back_populates="category")
    )
    income_transactions: Mapped[list["IncomeTransactions"]] = relationship(
        "IncomeTransactions", back_populates="category"
    )


class UserGoals(Base):
    __tablename__ = "user_goals"
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_goals_user"),
        PrimaryKeyConstraint("id", name="user_goals_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    target_goal: Mapped[str] = mapped_column(
        Enum("LIMIT EXPENSE", "SAVING", name="goal_target_enum"), nullable=False
    )
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(
        Enum("IN_PROGRESS", "FAILED", "PENDING", "SUCCESS", name="goal_status_enum"),
        nullable=False,
    )
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    user: Mapped["Users"] = relationship("Users", back_populates="user_goals")


class UserNotifications(Base):
    __tablename__ = "user_notifications"
    __table_args__ = (
        ForeignKeyConstraint(
            ["type_id"],
            ["notification_types.id"],
            name="user_notifications_type_id_fkey",
        ),
        ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="user_notifications_user_id_fkey"
        ),
        PrimaryKeyConstraint("id", name="user_notifications_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    type_id: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(
        Enum("PENDING", "SENT", "READ", "FAILED", name="user_notification_status_enum"),
        nullable=False,
        server_default=text("'PENDING'::user_notification_status_enum"),
    )
    scheduled_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(True), nullable=False, server_default=text("now()")
    )
    metadata_: Mapped[Optional[dict]] = mapped_column("metadata", JSONB)
    sent_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    read_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    type: Mapped["NotificationTypes"] = relationship(
        "NotificationTypes", back_populates="user_notifications"
    )
    user: Mapped["Users"] = relationship("Users", back_populates="user_notifications")


class UserPartnerProducts(Base):
    __tablename__ = "user_partner_products"
    __table_args__ = (
        ForeignKeyConstraint(
            ["partner_product_id"], ["partner_products.id"], name="fk_user_partner_prod"
        ),
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_partner_user"),
        PrimaryKeyConstraint("id", name="user_partner_products_pkey"),
        UniqueConstraint(
            "user_id",
            "partner_product_id",
            name="user_partner_products_user_id_partner_product_id_key",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    partner_product_id: Mapped[int] = mapped_column(Integer, nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    partner_product: Mapped["PartnerProducts"] = relationship(
        "PartnerProducts", back_populates="user_partner_products"
    )
    user: Mapped["Users"] = relationship(
        "Users", back_populates="user_partner_products"
    )


class UserSubscriptions(Base):
    __tablename__ = "user_subscriptions"
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_user_sub_user"),
        PrimaryKeyConstraint("id", name="user_subscriptions_pkey"),
        UniqueConstraint("user_id", name="user_subscriptions_user_id_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    plan_id: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(
        Enum(
            "ACTIVE",
            "CANCELLED",
            "TRIAL",
            "PAST_DUE",
            "EXPIRED",
            name="user_subscriptions_status",
        ),
        nullable=False,
    )
    renews_automatically: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("true")
    )
    last_payment_date: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(True)
    )
    next_billing_date: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(True)
    )
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    user: Mapped["Users"] = relationship("Users", back_populates="user_subscriptions")


class ExpensePlannedTransactions(Base):
    __tablename__ = "expense_planned_transactions"
    __table_args__ = (
        CheckConstraint("day BETWEEN 1 AND 31", name="valid_day_range"),
        ForeignKeyConstraint(
            ["category_id"], ["expense_categories.id"], name="fk_exp_plan_cat"
        ),
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_exp_plan_user"),
        PrimaryKeyConstraint("id", name="expense_planned_transactions_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, server_default=text("0")
    )
    day: Mapped[int] = mapped_column(Integer, nullable=False)
    interval: Mapped[str] = mapped_column(
        Enum(
            "WEEKLY",
            "MONTHLY",
            "BI_WEEKLY",
            "QUARTERLY",
            "HALF_YEAR",
            "YEARLY",
            name="expense_interval_enum",
        ),
        nullable=False,
    )
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    category: Mapped["ExpenseCategories"] = relationship(
        "ExpenseCategories", back_populates="expense_planned_transactions"
    )
    user: Mapped["Users"] = relationship(
        "Users", back_populates="expense_planned_transactions"
    )
    expense_planned_transaction_occurences: Mapped[
        list["ExpensePlannedTransactionOccurences"]
    ] = relationship("ExpensePlannedTransactionOccurences", back_populates="plan")


class ExpenseTransactions(Base):
    __tablename__ = "expense_transactions"
    __table_args__ = (
        CheckConstraint(
            "amount > 0::numeric", name="expense_transactions_amount_check"
        ),
        ForeignKeyConstraint(
            ["category_id"], ["expense_categories.id"], name="fk_exp_trans_cat"
        ),
        ForeignKeyConstraint(
            ["payment_method_id"],
            ["expense_payment_methods.id"],
            name="fk_exp_trans_payment",
        ),
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_exp_trans_user"),
        PrimaryKeyConstraint("id", name="expense_transactions_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    transaction_datetime: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    exclude_from_goal: Mapped[Optional[bool]] = mapped_column(
        Boolean, server_default=text("false")
    )
    note: Mapped[Optional[str]] = mapped_column(Text)
    payment_method_id: Mapped[Optional[int]] = mapped_column(Integer)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    category: Mapped["ExpenseCategories"] = relationship(
        "ExpenseCategories", back_populates="expense_transactions"
    )
    payment_method: Mapped[Optional["ExpensePaymentMethods"]] = relationship(
        "ExpensePaymentMethods", back_populates="expense_transactions"
    )
    user: Mapped["Users"] = relationship("Users", back_populates="expense_transactions")
    expense_planned_transaction_occurences: Mapped[
        list["ExpensePlannedTransactionOccurences"]
    ] = relationship(
        "ExpensePlannedTransactionOccurences", back_populates="transaction"
    )
    expense_transaction_attachments: Mapped[list["ExpenseTransactionAttachments"]] = (
        relationship("ExpenseTransactionAttachments", back_populates="transaction")
    )


class IncomePlannedTransactions(Base):
    __tablename__ = "income_planned_transactions"
    __table_args__ = (
        CheckConstraint("day BETWEEN 1 AND 31", name="valid_day_range"),
        ForeignKeyConstraint(
            ["category_id"], ["income_categories.id"], name="fk_income_plan_cat"
        ),
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_income_plan_user"),
        PrimaryKeyConstraint("id", name="income_planned_transactions_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    day: Mapped[int] = mapped_column(Integer, nullable=False)
    interval: Mapped[str] = mapped_column(
        Enum(
            "WEEKLY",
            "MONTHLY",
            "BI_WEEKLY",
            "QUARTERLY",
            "HALF_YEAR",
            "YEARLY",
            name="income_interval_enum",
        ),
        nullable=False,
    )
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    category: Mapped["IncomeCategories"] = relationship(
        "IncomeCategories", back_populates="income_planned_transactions"
    )
    user: Mapped["Users"] = relationship(
        "Users", back_populates="income_planned_transactions"
    )


class IncomeTransactions(Base):
    __tablename__ = "income_transactions"
    __table_args__ = (
        CheckConstraint("amount > 0::numeric", name="income_transactions_amount_check"),
        ForeignKeyConstraint(
            ["category_id"], ["income_categories.id"], name="fk_income_trans_cat"
        ),
        ForeignKeyConstraint(
            ["payment_method_id"],
            ["income_payment_methods.id"],
            name="fk_income_trans_payment",
        ),
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_income_trans_user"),
        PrimaryKeyConstraint("id", name="income_transactions_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    transaction_datetime: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=False
    )
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    exclude_from_goal: Mapped[Optional[bool]] = mapped_column(
        Boolean, server_default=text("false")
    )
    note: Mapped[Optional[str]] = mapped_column(Text)
    payment_method_id: Mapped[Optional[int]] = mapped_column(Integer)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    category: Mapped["IncomeCategories"] = relationship(
        "IncomeCategories", back_populates="income_transactions"
    )
    payment_method: Mapped[Optional["IncomePaymentMethods"]] = relationship(
        "IncomePaymentMethods", back_populates="income_transactions"
    )
    user: Mapped["Users"] = relationship("Users", back_populates="income_transactions")
    income_transaction_attachments: Mapped[list["IncomeTransactionAttachments"]] = (
        relationship("IncomeTransactionAttachments", back_populates="transaction")
    )


class ExpensePlannedTransactionOccurences(Base):
    __tablename__ = "expense_planned_transaction_occurences"
    __table_args__ = (
        ForeignKeyConstraint(
            ["plan_id"], ["expense_planned_transactions.id"], name="fk_exp_occur_plan"
        ),
        ForeignKeyConstraint(
            ["transaction_id"],
            ["expense_transactions.id"],
            ondelete="SET NULL",
            name="fk_exp_occur_trans",
        ),
        PrimaryKeyConstraint("id", name="expense_planned_transaction_occurences_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    plan_id: Mapped[int] = mapped_column(Integer, nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(
        Numeric(10, 2), nullable=False, server_default=text("0")
    )
    paid_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    transaction_id: Mapped[Optional[int]] = mapped_column(Integer)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    plan: Mapped["ExpensePlannedTransactions"] = relationship(
        "ExpensePlannedTransactions",
        back_populates="expense_planned_transaction_occurences",
    )
    transaction: Mapped[Optional["ExpenseTransactions"]] = relationship(
        "ExpenseTransactions", back_populates="expense_planned_transaction_occurences"
    )


class ExpenseTransactionAttachments(Base):
    __tablename__ = "expense_transaction_attachments"
    __table_args__ = (
        CheckConstraint(
            "content_length_bytes < 10485760",
            name="expense_transaction_attachments_content_length_bytes_check",
        ),
        ForeignKeyConstraint(
            ["transaction_id"], ["expense_transactions.id"], name="fk_exp_attach_trans"
        ),
        PrimaryKeyConstraint("id", name="expense_transaction_attachments_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transaction_id: Mapped[int] = mapped_column(Integer, nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(
        Enum("jpg", "png", "pdf", name="file_type_enum"), nullable=False
    )
    content_length_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    path: Mapped[str] = mapped_column(String(1024), nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    transaction: Mapped["ExpenseTransactions"] = relationship(
        "ExpenseTransactions", back_populates="expense_transaction_attachments"
    )


class IncomeTransactionAttachments(Base):
    __tablename__ = "income_transaction_attachments"
    __table_args__ = (
        ForeignKeyConstraint(
            ["transaction_id"],
            ["income_transactions.id"],
            name="fk_income_attach_trans",
        ),
        PrimaryKeyConstraint("id", name="income_transaction_attachments_pkey"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transaction_id: Mapped[int] = mapped_column(Integer, nullable=False)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    path: Mapped[str] = mapped_column(String(1024), nullable=False)
    last_modified_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP")
    )

    transaction: Mapped["IncomeTransactions"] = relationship(
        "IncomeTransactions", back_populates="income_transaction_attachments"
    )
