{{
    config(
        materialized='incremental',
        alias='stg_dim_loans',
        schema=var('gold_schema'),
        unique_key='loan_id',
        incremental_stragey='delete+insert'
    )
}}

SELECT
    loan_id,
    loan_type,
    loan_amount,
    interest_rate,
    getdate() as created_at
FROM
    {{ ref('stg_dim_loans') }}


{% if is_incremental() %}
WHERE created_at > (
    SELECT MAX(created_at)
    FROM {{ this }}
)
{% endif %}
