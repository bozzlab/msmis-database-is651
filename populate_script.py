import random
from model_factories.session import factory_session_scope


with factory_session_scope() as session:
    # script start here
    from model_factories.models import (
        UsersFactory,
        ExpenseCategoriesFactory,
        IncomeCategoriesFactory,
        ExpenseTransactionsFactory,
        ExpenseTransactionAttachmentsFactory,
        ExpensePlannedTransactionOccurencesFactory,
        IncomeTransactionsFactory,
        IncomeTransactionAttachmentsFactory,
        UserSubscriptionsFactory,
        UserGoalsFactory,
        UserPartnerProductsFactory,
        IncomePlannedTransactionsFactory,
        ExpensePlannedTransactionsFactory,
    )
    from model_factories.fake_data_map import (
        EXPENSE_CATEGORY_TRANSACTIONS_MAP,
        INCOME_CATEGORY_TRANSACTIONS_MAP,
    )
    from model_factories.helper import generate_mock_dates

    users = []

    for _ in range(100):
        user = UsersFactory()
        print(
            f"Created user: {user.id} - {user.email} {user.dob} {user.gender} {user.occupation.name}"
        )

        subscription = UserSubscriptionsFactory(user=user)
        print(
            f"Created subscription for user {user.id}: {subscription.id} - {subscription.subscription_plan.name}"
        )

        for _ in range(random.randint(1, 5)):
            user_partner = UserPartnerProductsFactory(user=user)
            print(
                f"Created partner product for user {user.id}: {user_partner.partner_product.partner.name} - {user_partner.partner_product.type}"
            )

        for name in random.sample(
            list(EXPENSE_CATEGORY_TRANSACTIONS_MAP.keys()),
            k=random.randint(5, len(EXPENSE_CATEGORY_TRANSACTIONS_MAP)),
        ):
            category = ExpenseCategoriesFactory(user=user, name=name)
            print(
                f"Created expense category for user {user.id}: {category.id} - {category.name}"
            )

        for name in random.sample(
            list(INCOME_CATEGORY_TRANSACTIONS_MAP.keys()),
            k=random.randint(5, len(INCOME_CATEGORY_TRANSACTIONS_MAP)),
        ):
            category = IncomeCategoriesFactory(user=user, name=name)
            print(
                f"Created income category for user {user.id}: {category.id} - {category.name}"
            )

        date_range = generate_mock_dates(min_per_month=10, max_per_month=25)
        print(f"Generated {len(date_range)} mock transaction dates for user {user.id}")
        print("start date:", date_range[0], "end date:", date_range[-1])

        for date in date_range:
            expense = ExpenseTransactionsFactory(user=user, transaction_datetime=date, payment_method_id=random.randint(1,3))
            print(
                f"Created expense transaction for user {user.id}: [{date}] {expense.id} - [{expense.category.name}] {expense.name} - {expense.amount}"
            )

            if random.random() < 0.2:
                for _ in range(2):
                    attachment = ExpenseTransactionAttachmentsFactory(
                        transaction=expense
                    )
                    print(
                        f"Created expense attachment: {attachment.id} - {attachment.filename} - {attachment.path}"
                    )

        date_range = generate_mock_dates(min_per_month=1, max_per_month=2)
        print(f"Generated {len(date_range)} mock transaction dates for user {user.id}")
        print("start date:", date_range[0], "end date:", date_range[-1])

        for date in date_range:
            income = IncomeTransactionsFactory(user=user, transaction_datetime=date)
            print(
                f"Created income transaction for user {user.id}: [{date}] {income.id} - [{income.category.name}] {income.name} - {income.amount}"
            )

            if random.random() < 0.00002:
                for _ in range(2):
                    attachment = IncomeTransactionAttachmentsFactory(transaction=income)
                    print(
                        f"Created income attachment: {attachment.id} - {attachment.filename} - {attachment.path}"
                    )

        for target_goal in ["SAVING", "LIMIT EXPENSE"]:
            goal = UserGoalsFactory(user=user, target_goal=target_goal)
            print(
                f"Created user goal for user {user.id}: {goal.id} - [{goal.target_goal}] {goal.name}  - {goal.amount}"
            )

        for _ in range(random.randint(1, 3)):
            planned_expense = ExpensePlannedTransactionsFactory(user=user)
            print(
                f"Created planned expense transaction for user {user.id}: {planned_expense.id} [at {planned_expense.day} of month] - {planned_expense.name} - {planned_expense.amount}: range: [{planned_expense.start_date} - {planned_expense.end_date}]"
            )

            if planned_expense.start_date and planned_expense.end_date:
                for _ in range(random.randint(1, 5)):
                    ept = ExpensePlannedTransactionOccurencesFactory(
                        user=user, plan=planned_expense
                    )
                    print(
                        f"Created planned expense transaction occurence for user {user.id}: {planned_expense.id}: {ept.id} - {ept.paid_date} - {ept.amount}"
                    )

        for _ in range(random.randint(1, 3)):
            planned_income = IncomePlannedTransactionsFactory(user=user)
            print(
                f"Created planned income transaction for user {user.id}: {planned_income.id} - [at {planned_income.day} of month]  {planned_income.name} - {planned_income.amount}"
            )
