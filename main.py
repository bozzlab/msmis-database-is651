from app.model_factories.session import factory_session_scope


with factory_session_scope():
    # script start here
    from app.model_factories.models import (
        UsersFactory,
        ExpenseCategoriesFactory,
        IncomeCategoriesFactory,
        ExpenseTransactionsFactory,
        IncomeTransactionsFactory,
        UserGoalsFactory,
        IncomePlannedTransactionsFactory,
        ExpensePlannedTransactionsFactory,
    )

    users = []

    for _ in range(5):
        user = UsersFactory()
        print(f"Created user: {user.id} - {user.email}")
        users.append(user)

    for user in users:
        for _ in range(3):
            category = ExpenseCategoriesFactory(user=user)
            print(
                f"Created expense category for user {user.id}: {category.id} - {category.name}"
            )

        for _ in range(3):
            category = IncomeCategoriesFactory(user=user)
            print(
                f"Created income category for user {user.id}: {category.id} - {category.name}"
            )

    for user in users:
        for _ in range(10):
            expense = ExpenseTransactionsFactory(user=user)
            print(
                f"Created expense transaction for user {user.id}: {expense.id} - {expense.name} - {expense.amount}"
            )

        for _ in range(10):
            income = IncomeTransactionsFactory(user=user)
            print(
                f"Created income transaction for user {user.id}: {income.id} - {income.name} - {income.amount}"
            )

    for user in users:
        goal = UserGoalsFactory(user=user)
        print(
            f"Created user goal for user {user.id}: {goal.id} - {goal.name} [{goal.target_goal}] - {goal.amount}"
        )

    for user in users:
        planned_expense = ExpensePlannedTransactionsFactory(user=user)
        print(
            f"Created planned expense transaction for user {user.id}: {planned_expense.id} - {planned_expense.name} - {planned_expense.amount}"
        )
        planned_income = IncomePlannedTransactionsFactory(user=user)
        print(
            f"Created planned income transaction for user {user.id}: {planned_income.id} - {planned_income.name} - {planned_income.amount}"
        )
