{{
    config(
        materialized='incremental',
        alias='dim_investment_type',
        schema=var('gold_schema'),
        unique_key='investment_type_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    investment_type_id,
    INITCAP(investment_type_name) AS investment_type_name,
    created_at
FROM
    {{ ref('stg_dim_investment_type') }}




