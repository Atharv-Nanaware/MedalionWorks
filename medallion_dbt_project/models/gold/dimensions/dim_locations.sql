{{
    config(
        materialized='incremental',
        alias='dim_location',
        schema=var('gold_schema'),
        unique_key='location_id',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    location_id,
    city,
    state,
    country,
    postal_code,
    created_at
FROM
    {{ ref('stg_dim_location') }}


