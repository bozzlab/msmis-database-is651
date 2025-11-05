from app.model_factories.session import factory_session_scope


with factory_session_scope():
    # script start here
    from app.model_factories.models import (
        UsersFactory,
        ExpenseCategoriesFactory,
        IncomeCategoriesFactory,
        ExpenseTransactionsFactory,
        IncomeTransactionsFactory,
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
