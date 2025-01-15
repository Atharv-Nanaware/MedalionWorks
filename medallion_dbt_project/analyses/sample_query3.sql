

-- Average Investment Return by Investment Type

SELECT
    investment_type_name,
    ROUND(AVG(investment_return), 2) AS avg_investment_return
FROM
    {{ ref('fact_investments') }}
GROUP BY 1
ORDER BY avg_investment_return DESC;
