-- SELECT all categories from both income and expense categories tables (will be create as view table)
WITH categories AS (
  SELECT 
    ic.user_id,
    'income category' AS type,
    ic.name
  FROM income_categories ic
  GROUP BY ic.user_id, ic.name
  UNION ALL
  SELECT 
    ec.user_id,
    'expense category' AS type,
    ec.name
  FROM expense_categories ec
  GROUP BY ec.user_id, ec.name
  ORDER BY user_id, type, name
)

-- output 

-- | user_id | type             | name       |
-- | ------- | ---------------- | ---------- |
-- | 1       | expense category | Bills      |
-- | 1       | expense category | Food       |
-- | 1       | expense category | Shopping   |
-- | 1       | expense category | Transport  |
-- | 1       | income category  | Bonus      |
-- | 1       | income category  | Freelance  |
-- | 1       | income category  | Investment |
-- | 1       | income category  | Salary     |
-- | 2       | expense category | Bills      |
-- | 2       | expense category | Food       |
-- | 2       | expense category | Shopping   |
-- | 2       | expense category | Transport  |
-- | 2       | income category  | Bonus      |


-- Usage
---- Get all categories for user with user_id = 3

SELECT 
  type,
  name
FROM categories
WHERE user_id = 3
ORDER BY type, name;

-- | type             | name      |
-- | ---------------- | --------- |
-- | expense category | Food      |
-- | expense category | Shopping  |
-- | expense category | Transport |
-- | income category  | Bonus     |
-- | income category  | Freelance |
-- | income category  | Salary    |
