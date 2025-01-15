-- Ensure no account has a negative balance. This is crucial for account integrity.
SELECT account_id
FROM {{ ref('dim_account') }}
WHERE account_balance < 0;
