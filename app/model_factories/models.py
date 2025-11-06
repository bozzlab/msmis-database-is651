import factory

import random

from app.models import models
from .fake_data_map import (
    EXPENSE_CATEGORY_TRANSACTIONS_MAP,
    INCOME_CATEGORY_TRANSACTIONS_MAP,
)
from .helper import get_random_existing
from .base import BaseFactory


class CurrenciesFactory(BaseFactory):
    class Meta:
        model = models.Currencies

    code = factory.Sequence(lambda n: f"C{n:03d}")
    name = factory.Faker("currency_name")
    active = True


class EducationLevelsFactory(BaseFactory):
    class Meta:
        model = models.EducationLevels

    level = factory.Iterator(["High School", "Bachelor", "Master", "PhD"])


class ExpensePaymentMethodsFactory(BaseFactory):
    class Meta:
        model = models.ExpensePaymentMethods

    name = factory.Iterator(["Credit Card", "Cash", "Bank Transfer"])
    is_active = True


class IncomePaymentMethodsFactory(BaseFactory):
    class Meta:
        model = models.IncomePaymentMethods

    name = factory.Iterator(["Salary Deposit", "Cash", "Bank Transfer"])
    is_active = True


class NotificationTypesFactory(BaseFactory):
    class Meta:
        model = models.NotificationTypes

    name = factory.Sequence(lambda n: f"Notification Type {n}")
    delivery_channel = factory.Iterator(["EMAIL", "APP_PUSH", "SMS"])
    template_title = factory.Faker("sentence")
    template_body = factory.Faker("paragraph")


class OccupationsFactory(BaseFactory):
    class Meta:
        model = models.Occupations

    name = factory.Faker("job")


class PartnersFactory(BaseFactory):
    class Meta:
        model = models.Partners

    name = factory.Sequence(lambda n: f"Partner Inc. {n}")
    is_active = True


class PostalCodesFactory(BaseFactory):
    class Meta:
        model = models.PostalCodes

    postal_code = factory.Sequence(lambda n: f"{n:05d}")


class SubscriptionPlansFactory(BaseFactory):
    class Meta:
        model = models.SubscriptionPlans

    name = factory.Sequence(lambda n: f"Plan {n}")
    price = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    billing_cycle = factory.Iterator(["MONTHLY", "YEARLY"])
    is_active = True
    features = factory.Faker("pydict", nb_elements=3, value_types=["str", "bool"])


class WorkExperienceLevelsFactory(BaseFactory):
    class Meta:
        model = models.WorkExperienceLevels

    level = factory.Iterator(["Entry Level", "Mid Level", "Senior", "Lead"])


class PartnerProductsFactory(BaseFactory):
    class Meta:
        model = models.PartnerProducts

    partner = factory.SubFactory(PartnersFactory)

    type = factory.Faker("word")
    remark = factory.Faker("sentence")
    is_active = True


class UsersFactory(BaseFactory):
    class Meta:
        model = models.Users

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    username = factory.LazyAttributeSequence(
        lambda o, n: f"{o.first_name.lower()}-{o.last_name.lower()}{n}"
    )
    password_hash = factory.Faker("password", length=60)
    email = factory.LazyAttribute(
        lambda o: o.username
        + "@"
        + random.choice(
            ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "msmis.com"]
        )
    )

    phone_number = factory.Faker("phone_number")
    dob = factory.Faker("date_of_birth", minimum_age=18, maximum_age=65)
    gender = factory.Iterator(["F", "M", "Others", "Rather not to say"])
    personal_data_consent = factory.Faker("boolean", chance_of_getting_true=80)
    marketing_consent = factory.Faker("boolean", chance_of_getting_true=50)

    occupation = factory.LazyFunction(lambda: get_random_existing(models.Occupations))
    work_experience_level = factory.LazyFunction(
        lambda: get_random_existing(models.WorkExperienceLevels)
    )
    education_level = factory.LazyFunction(
        lambda: get_random_existing(models.EducationLevels)
    )
    postal_code = factory.LazyFunction(lambda: get_random_existing(models.PostalCodes))
    currency = factory.LazyFunction(lambda: get_random_existing(models.Currencies))


class ExpenseCategoriesFactory(BaseFactory):
    class Meta:
        model = models.ExpenseCategories

    name = factory.LazyAttribute(
        lambda _: random.choice(list(EXPENSE_CATEGORY_TRANSACTIONS_MAP.keys()))
    )
    user = factory.SubFactory(UsersFactory)


class IncomeCategoriesFactory(BaseFactory):
    class Meta:
        model = models.IncomeCategories

    name = factory.LazyAttribute(
        lambda _: random.choice(list(INCOME_CATEGORY_TRANSACTIONS_MAP.keys()))
    )
    user = factory.SubFactory(UsersFactory)


class UserGoalsFactory(BaseFactory):
    class Meta:
        model = models.UserGoals

    user = factory.SubFactory(UsersFactory)
    name = factory.Faker("bs")
    target_goal = factory.Iterator(["LIMIT EXPENSE", "SAVING"])
    amount = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    start_date = factory.Faker("date_this_year")
    end_date = factory.Faker("date_between", start_date="+1y", end_date="+2y")
    status = (
        "PENDING"  # factory.Iterator(["PENDING", "SUCCESS", "IN_PROGRESS", "FAILED"])
    )


class UserNotificationsFactory(BaseFactory):
    class Meta:
        model = models.UserNotifications

    user = factory.SubFactory(UsersFactory)
    type = factory.SubFactory(NotificationTypesFactory)
    status = factory.Iterator(["PENDING", "SENT", "READ", "FAILED"])
    scheduled_at = factory.Faker("date_time_this_month")
    metadata_ = factory.Faker("pydict", nb_elements=2)


class UserPartnerProductsFactory(BaseFactory):
    class Meta:
        model = models.UserPartnerProducts
        sqlalchemy_get_or_create = ("user", "partner_product")

    user = factory.SubFactory(UsersFactory)
    partner_product = factory.SubFactory(PartnerProductsFactory)


class UserSubscriptionsFactory(BaseFactory):
    class Meta:
        model = models.UserSubscriptions
        sqlalchemy_get_or_create = ("user",)

    user = factory.SubFactory(UsersFactory)
    plan_id = factory.SelfAttribute("subscription_plan.id")
    status = factory.Iterator(["ACTIVE", "TRIAL", "CANCELLED"])
    renews_automatically = True
    next_billing_date = factory.Faker("date_time_this_month")

    subscription_plan = factory.SubFactory(SubscriptionPlansFactory)


class ExpensePlannedTransactionsFactory(BaseFactory):
    class Meta:
        model = models.ExpensePlannedTransactions

    user = factory.SubFactory(UsersFactory)
    category = factory.SubFactory(
        ExpenseCategoriesFactory, user=factory.SelfAttribute("..user")
    )

    name = factory.Faker("bs")
    amount = factory.Faker("pydecimal", left_digits=3, right_digits=2, positive=True)
    day = random.choice(range(1, 31))
    interval = factory.Iterator(["WEEKLY", "MONTHLY", "YEARLY"])
    start_date = factory.Faker("date_this_year")
    end_date = factory.Faker("date_between", start_date="+1y", end_date="+2y")


class ExpenseTransactionsFactory(BaseFactory):
    class Meta:
        model = models.ExpenseTransactions

    user = factory.SubFactory(UsersFactory)
    category = factory.SubFactory(
        ExpenseCategoriesFactory, user=factory.SelfAttribute("..user")
    )

    payment_method = factory.LazyFunction(
        lambda: get_random_existing(models.ExpensePaymentMethods)
    )

    transaction_datetime = factory.Faker("date_time_this_year")
    name = factory.LazyAttribute(
        lambda o: random.choice(EXPENSE_CATEGORY_TRANSACTIONS_MAP[o.category.name])
    )
    amount = factory.Faker(
        "pydecimal", left_digits=3, right_digits=2, positive=True, min_value=1
    )
    exclude_from_goal = False
    note = factory.Faker("sentence")


class IncomePlannedTransactionsFactory(BaseFactory):
    class Meta:
        model = models.IncomePlannedTransactions

    user = factory.SubFactory(UsersFactory)
    category = factory.SubFactory(
        IncomeCategoriesFactory, user=factory.SelfAttribute("..user")
    )

    name = factory.Faker("bs")
    amount = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    day = random.choice(range(1, 31))
    interval = factory.Iterator(["WEEKLY", "MONTHLY", "YEARLY"])


class IncomeTransactionsFactory(BaseFactory):
    class Meta:
        model = models.IncomeTransactions

    user = factory.SubFactory(UsersFactory)
    category = factory.SubFactory(
        IncomeCategoriesFactory, user=factory.SelfAttribute("..user")
    )
    payment_method = factory.LazyFunction(
        lambda: get_random_existing(models.IncomePaymentMethods)
    )

    transaction_datetime = factory.Faker("date_time_this_year")
    amount = factory.Faker(
        "pydecimal", left_digits=4, right_digits=2, positive=True, min_value=1
    )
    name = factory.LazyAttribute(
        lambda o: random.choice(INCOME_CATEGORY_TRANSACTIONS_MAP[o.category.name])
    )
    exclude_from_goal = False
    note = factory.Faker("sentence")


class ExpensePlannedTransactionOccurencesFactory(BaseFactory):
    class Meta:
        model = models.ExpensePlannedTransactionOccurences

    plan = factory.SubFactory(ExpensePlannedTransactionsFactory)

    transaction = factory.Maybe(
        factory.Faker("boolean", chance_of_getting_true=50),
        yes_declaration=factory.SubFactory(
            ExpenseTransactionsFactory, user=factory.SelfAttribute("..plan.user")
        ),
        no_declaration=None,
    )

    amount = factory.SelfAttribute("plan.amount")
    paid_date = factory.SelfAttribute("plan.date")


class ExpenseTransactionAttachmentsFactory(BaseFactory):
    class Meta:
        model = models.ExpenseTransactionAttachments

    transaction = factory.SubFactory(ExpenseTransactionsFactory)
    filename = factory.Faker("file_name", extension="jpg")
    file_type = factory.Iterator(["jpg", "png", "pdf"])
    content_length_bytes = factory.Faker("pyint", min_value=1000, max_value=5000000)
    path = factory.Faker("file_path", depth=3, extension="jpg")


class IncomeTransactionAttachmentsFactory(BaseFactory):
    class Meta:
        model = models.IncomeTransactionAttachments

    transaction = factory.SubFactory(IncomeTransactionsFactory)
    filename = factory.Faker("file_name", extension="pdf")
    path = factory.Faker("file_path", depth=3, extension="pdf")
    content_length_bytes = factory.Faker("pyint", min_value=1000, max_value=5000000)
    path = factory.Faker("file_path", depth=3, extension="jpg")
