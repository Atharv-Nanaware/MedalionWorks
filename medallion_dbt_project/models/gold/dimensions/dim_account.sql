{{
    config(
        materialized='incremental',
        alias='dim_account',
        schema=var('gold_schema'),
        unique_key='account_id',
        incremental_strategy='delete+insert'
    )
}}

WITH base_data AS (
    SELECT
        account_id,
        customer_id,
        account_number,
        account_type,
        account_balance,
        credit_score,
        created_at
    FROM {{ ref('stg_dim_account') }}
)

SELECT *
FROM base_data

