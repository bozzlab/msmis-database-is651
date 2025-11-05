START TRANSACTION;

-- ------------------
-- 1. Drop All Tables
-- ------------------

DROP TABLE IF EXISTS
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
CASCADE;

-- ------------------
-- 2. Drop Trigger Function
-- ------------------
DROP FUNCTION IF EXISTS update_last_modified_at_column() CASCADE;

-- ------------------
-- 3. Drop All ENUM Types
-- ------------------
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

COMMIT;