-- View full dataset
SELECT * FROM sales_data;

-- Total revenue
SELECT
    SUM(quantity * price) AS total_revenue
FROM sales_data;

-- Revenue by product
SELECT
    product,
    SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY product
ORDER BY revenue DESC;

-- Revenue by region
SELECT
    region,
    SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY region
ORDER BY revenue DESC;

-- Revenue by category
SELECT
    category,
    SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY category
ORDER BY revenue DESC;

-- Monthly revenue trend
SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(quantity * price) AS revenue
FROM sales_data
GROUP BY month
ORDER BY month;