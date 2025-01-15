-- Validate that only valid account types are used (Savings, Checking, Investment, Loan).
SELECT
    account_id,
    account_type
FROM {{ ref('dim_account') }}
WHERE account_type NOT IN ('Savings', 'Checking', 'Investment', 'Loan');
