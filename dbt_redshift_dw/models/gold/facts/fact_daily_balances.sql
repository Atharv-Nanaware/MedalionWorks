{{
    config(
        materialized='view',
        alias='fact_daily_balances',
        schema=var('gold_schema')
    )
}}

WITH source_data AS (
    SELECT
        balance_id,
        date_id,
        account_id,
        currency_id,
        opening_balance,
        closing_balance,
        average_balance
    FROM {{ ref('stg_fact_daily_balances') }}
)

SELECT
    s.date_id,
    s.balance_id,
    d.date AS balance_date,
    s.account_id,
    a.account_number,
    a.account_type,
    a.credit_score,
    c.currency_code,
    c.currency_name,
    s.opening_balance,
    s.closing_balance,
    s.average_balance
FROM source_data s
INNER JOIN {{ ref('dim_date') }} AS d ON s.date_id = d.date_id
INNER JOIN {{ ref('dim_account') }} AS a ON s.account_id = a.account_id
INNER JOIN {{ ref('dim_currency') }} AS c ON s.currency_id = c.currency_id
