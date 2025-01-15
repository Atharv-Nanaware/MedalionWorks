
-- Total Investment Amount By Year

SELECT
    EXTRACT(YEAR FROM to_date(investment_date, 'yyyy-mm-dd')) AS year,
    SUM(investment_amount) AS total_investment_amount
FROM
    {{ ref('fact_investments') }}
GROUP BY 1
ORDER BY 1;
