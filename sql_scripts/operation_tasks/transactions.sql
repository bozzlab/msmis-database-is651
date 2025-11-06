-- 1. Get summary transactions all users (will be create as VIEW table)

WITH summary_transactions AS (
SELECT
  u.id AS user_id,

  -- Today
  COALESCE(SUM(e.amount) FILTER (WHERE DATE(e.transaction_datetime) = CURRENT_DATE), 0) AS today_total_exp,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE(i.transaction_datetime) = CURRENT_DATE), 0) AS today_total_inc,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE(i.transaction_datetime) = CURRENT_DATE), 0)
    - COALESCE(SUM(e.amount) FILTER (WHERE DATE(e.transaction_datetime) = CURRENT_DATE), 0) AS today_total_net,

  -- Weekly
  COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('week', e.transaction_datetime) = DATE_TRUNC('week', CURRENT_DATE)), 0) AS week_total_exp,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('week', i.transaction_datetime) = DATE_TRUNC('week', CURRENT_DATE)), 0) AS week_total_inc,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('week', i.transaction_datetime) = DATE_TRUNC('week', CURRENT_DATE)), 0)
    - COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('week', e.transaction_datetime) = DATE_TRUNC('week', CURRENT_DATE)), 0) AS week_total_net,

  -- Monthly
  COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('month', e.transaction_datetime) = DATE_TRUNC('month', CURRENT_DATE)), 0) AS monthly_total_exp,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('month', i.transaction_datetime) = DATE_TRUNC('month', CURRENT_DATE)), 0) AS monthly_total_inc,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('month', i.transaction_datetime) = DATE_TRUNC('month', CURRENT_DATE)), 0)
    - COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('month', e.transaction_datetime) = DATE_TRUNC('month', CURRENT_DATE)), 0) AS monthly_total_net,

  -- Quarterly
  COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('quarter', e.transaction_datetime) = DATE_TRUNC('quarter', CURRENT_DATE)), 0) AS quarterly_total_exp,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('quarter', i.transaction_datetime) = DATE_TRUNC('quarter', CURRENT_DATE)), 0) AS quarterly_total_inc,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('quarter', i.transaction_datetime) = DATE_TRUNC('quarter', CURRENT_DATE)), 0)
    - COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('quarter', e.transaction_datetime) = DATE_TRUNC('quarter', CURRENT_DATE)), 0) AS quarterly_total_net,

  -- Half Yearly
  COALESCE(SUM(e.amount) FILTER (
      WHERE ((EXTRACT(MONTH FROM e.transaction_datetime)-1)/6)::int = ((EXTRACT(MONTH FROM CURRENT_DATE)-1)/6)::int
        AND EXTRACT(YEAR FROM e.transaction_datetime) = EXTRACT(YEAR FROM CURRENT_DATE)
  ), 0) AS half_year_total_exp,
  COALESCE(SUM(i.amount) FILTER (
      WHERE ((EXTRACT(MONTH FROM i.transaction_datetime)-1)/6)::int = ((EXTRACT(MONTH FROM CURRENT_DATE)-1)/6)::int
        AND EXTRACT(YEAR FROM i.transaction_datetime) = EXTRACT(YEAR FROM CURRENT_DATE)
  ), 0) AS half_year_total_inc,
  COALESCE(SUM(i.amount) FILTER (
      WHERE ((EXTRACT(MONTH FROM i.transaction_datetime)-1)/6)::int = ((EXTRACT(MONTH FROM CURRENT_DATE)-1)/6)::int
        AND EXTRACT(YEAR FROM i.transaction_datetime) = EXTRACT(YEAR FROM CURRENT_DATE)
  ), 0)
    - COALESCE(SUM(e.amount) FILTER (
      WHERE ((EXTRACT(MONTH FROM e.transaction_datetime)-1)/6)::int = ((EXTRACT(MONTH FROM CURRENT_DATE)-1)/6)::int
        AND EXTRACT(YEAR FROM e.transaction_datetime) = EXTRACT(YEAR FROM CURRENT_DATE)
  ), 0) AS half_year_total_net,

  -- Yearly
  COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('year', e.transaction_datetime) = DATE_TRUNC('year', CURRENT_DATE)), 0) AS yearly_total_exp,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('year', i.transaction_datetime) = DATE_TRUNC('year', CURRENT_DATE)), 0) AS yearly_total_inc,
  COALESCE(SUM(i.amount) FILTER (WHERE DATE_TRUNC('year', i.transaction_datetime) = DATE_TRUNC('year', CURRENT_DATE)), 0)
    - COALESCE(SUM(e.amount) FILTER (WHERE DATE_TRUNC('year', e.transaction_datetime) = DATE_TRUNC('year', CURRENT_DATE)), 0) AS yearly_total_net

FROM users u
LEFT JOIN expense_transactions e ON u.id = e.user_id
LEFT JOIN income_transactions i ON u.id = i.user_id
GROUP BY u.id
ORDER BY u.id
)

-- Output 

-- | user_id | today_total_exp | today_total_inc | today_total_net | week_total_exp | week_total_inc | week_total_net | monthly_total_exp | monthly_total_inc | monthly_total_net | quarterly_total_exp | quarterly_total_inc | quarterly_total_net | half_year_total_exp | half_year_total_inc | half_year_total_net | yearly_total_exp | yearly_total_inc | yearly_total_net |
-- | ------- | --------------- | --------------- | --------------- | -------------- | -------------- | -------------- | ----------------- | ----------------- | ----------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ---------------- | ---------------- | ---------------- |
-- | 1       | 338.11          | 0               | -338.11         | 4820.14        | 0              | -4820.14       | 5984.89           | 0                 | -5984.89          | 5984.89             | 0                   | -5984.89            | 5984.89             | 0                   | -5984.89            | 5984.89          | 0                | -5984.89         |
-- | 2       | 0               | 0               | 0               | 0              | 0              | 0              | 0                 | 0                 | 0                 | 0                   | 0                   | 0                   | 0                   | 0                   | 0                   | 0                | 0                | 0                |
-- | 3       | 0               | 0               | 0               | 0              | 0              | 0              | 0                 | 0                 | 0                 | 0                   | 0                   | 0                   | 0                   | 0                   | 0                   | 0                | 0                | 0                |
-- | 4       | 0               | 0               | 0               | 0              | 0              | 0              | 0                 | 0                 | 0                 | 0                   | 0                   | 0                   | 0                   | 0                   | 0                   | 0                | 0                | 0                |
-- | 5       | 0               | 0               | 0               | 0              | 0              | 0              | 0                 | 0                 | 0                 | 0                   | 0                   | 0                   | 0                   | 0                   | 0                   | 0                | 0                | 0                |
-- | 6       | 0               | 0               | 0               | 48503.50       | 248976.90      | 200473.40      | 64905.20          | 523853.20         | 458948.00         | 64905.20            | 523853.20           | 458948.00           | 64905.20            | 523853.20           | 458948.00           | 64905.20         | 523853.20        | 458948.00        |
-- | 7       | 7064.70         | 58045.90        | 50981.20        | 34376.40       | 493300.80      | 458924.40      | 46758.10          | 640792.50         | 594034.40         | 46758.10            | 640792.50           | 594034.40           | 46758.10            | 640792.50           | 594034.40           | 46758.10         | 640792.50        | 594034.40        |
-- | 8       | 14131.80        | 22571.90        | 8440.10         | 28678.10       | 194402.10      | 165724.00      | 47822.20          | 622102.70         | 574280.50         | 47822.20            | 622102.70           | 574280.50           | 47822.20            | 622102.70           | 574280.50           | 47822.20         | 622102.70        | 574280.50        |
-- | 9       | 6677.00         | 122959.60       | 116282.60       | 37539.40       | 468504.10      | 430964.70      | 62120.60          | 605182.60         | 543062.00         | 62120.60            | 605182.60           | 543062.00           | 62120.60            | 605182.60           | 543062.00           | 62120.60         | 605182.60        | 543062.00        |
-- | 10      | 3974.60         | 167035.60       | 163061.00       | 33817.60       | 306500.50      | 272682.90      | 47146.20          | 683369.30         | 636223.10         | 47146.20            | 683369.30           | 636223.10           | 47146.20            | 683369.30           | 636223.10           | 47146.20         | 683369.30        | 636223.10        |

-- Usage 
---- Get today summary transaction for user_id = 10

SELECT today_total_inc, today_total_exp, today_total_net FROM summary_transactions
WHERE user_id = 10

-- | today_total_inc | today_total_exp | today_total_net |
-- | --------------- | --------------- | --------------- |
-- | 167035.60       | 3974.60         | 163061.00       |


-- 2. Get specific range with specific user 


