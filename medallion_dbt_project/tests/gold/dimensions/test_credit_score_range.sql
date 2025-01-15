-- Ensure credit scores fall within the valid range of 300 to 850.
SELECT
    account_id,
    credit_score
FROM {{ ref('dim_account') }}
WHERE credit_score < 300 OR credit_score > 850;
