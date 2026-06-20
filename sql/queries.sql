SELECT amfi_code, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT AVG(nav) AS avg_nav
FROM fact_nav;

SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

SELECT amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT AVG(aum_crore)
FROM fact_performance;

SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

SELECT city,
COUNT(*) AS total
FROM fact_transactions
GROUP BY city
ORDER BY total DESC
LIMIT 10;
