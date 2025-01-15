{{
    config(
        materialized='incremental',
        alias='dim_transaction_type',
        schema=var('gold_schema'),
        unique_key='transaction_type_id',
        incremental_strategy='delete+insert'
    )
}}

WITH base_data AS (
    SELECT
        transaction_type_id,
        INITCAP(transaction_type_name) AS transaction_type_name,
        created_at
    FROM {{ ref('stg_dim_transaction_type') }}
)

SELECT *
FROM base_data

{% if is_incremental() %}
WHERE created_at > (
    SELECT MAX(created_at)
    FROM {{ this }}
)
{% endif %}
