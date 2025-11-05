START TRANSACTION;

TRUNCATE TABLE
    occupations,
    work_experience_levels,
    postal_codes,
    education_levels,
    currencies,
    partners,
    partner_products,
    users,
    subscription_plans,
    user_subscriptions,
    notification_types,
    user_notifications,
    user_goals,
    user_partner_products,
    income_payment_methods,
    income_categories,
    income_transactions,
    income_transaction_attachments,
    income_planned_transactions,
    expense_payment_methods,
    expense_categories,
    expense_transactions,
    expense_transaction_attachments,
    expense_planned_transactions,
    expense_planned_transaction_occurences
RESTART IDENTITY CASCADE;

COMMIT;