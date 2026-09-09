-- Retail Sales & Inventory Analytics
-- PostgreSQL / standard SQL-friendly query set

-- 01. Overall KPIs
SELECT
    COUNT(DISTINCT order_id) AS orders,
    SUM(quantity) AS units_sold,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    SUM(profit) / NULLIF(SUM(net_sales), 0) AS margin_pct,
    SUM(net_sales) / NULLIF(COUNT(DISTINCT order_id), 0) AS avg_order_value
FROM sales;

-- 02. Monthly revenue and profit trend
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    SUM(profit) / NULLIF(SUM(net_sales),0) AS margin_pct,
    COUNT(DISTINCT order_id) AS orders
FROM sales
GROUP BY 1
ORDER BY 1;

-- 03. Category performance
SELECT
    category,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    SUM(quantity) AS units_sold,
    SUM(profit) / NULLIF(SUM(net_sales),0) AS margin_pct
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 04. Top products by revenue
SELECT
    product_id,
    product_name,
    category,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    SUM(quantity) AS units_sold
FROM sales
GROUP BY product_id, product_name, category
ORDER BY revenue DESC
LIMIT 15;

-- 05. Low-margin products with meaningful revenue
SELECT
    product_id,
    product_name,
    category,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    SUM(profit) / NULLIF(SUM(net_sales),0) AS margin_pct
FROM sales
GROUP BY product_id, product_name, category
HAVING SUM(net_sales) >= 1000
ORDER BY margin_pct ASC, revenue DESC;

-- 06. Channel performance
SELECT
    sales_channel,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    COUNT(DISTINCT order_id) AS orders,
    SUM(net_sales) / NULLIF(COUNT(DISTINCT order_id),0) AS avg_order_value
FROM sales
GROUP BY sales_channel
ORDER BY revenue DESC;

-- 07. Regional performance
SELECT
    region,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    COUNT(DISTINCT order_id) AS orders
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- 08. Monthly product revenue using a CTE
WITH product_month AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        product_id,
        product_name,
        SUM(net_sales) AS revenue
    FROM sales
    GROUP BY 1,2,3
), ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY month ORDER BY revenue DESC) AS rn
    FROM product_month
)
SELECT *
FROM ranked
WHERE rn <= 5
ORDER BY month, rn;

-- 09. Inventory risk summary
SELECT
    product_id,
    product_name,
    category,
    supplier,
    AVG(days_of_cover) AS avg_days_cover,
    MIN(closing_stock) AS min_closing_stock,
    SUM(CASE WHEN stock_status = 'Stockout' THEN 1 ELSE 0 END) AS stockout_months,
    SUM(CASE WHEN stock_status = 'Low Stock' THEN 1 ELSE 0 END) AS low_stock_months,
    SUM(CASE WHEN stock_status = 'Overstock' THEN 1 ELSE 0 END) AS overstock_months
FROM inventory_snapshot
GROUP BY product_id, product_name, category, supplier
ORDER BY stockout_months DESC, overstock_months DESC;

-- 10. High-risk inventory candidates
WITH inventory_summary AS (
    SELECT
        product_id,
        product_name,
        category,
        supplier,
        SUM(CASE WHEN stock_status = 'Stockout' THEN 1 ELSE 0 END) AS stockout_months,
        SUM(CASE WHEN stock_status = 'Low Stock' THEN 1 ELSE 0 END) AS low_stock_months,
        SUM(CASE WHEN stock_status = 'Overstock' THEN 1 ELSE 0 END) AS overstock_months,
        AVG(days_of_cover) AS avg_days_cover
    FROM inventory_snapshot
    GROUP BY product_id, product_name, category, supplier
)
SELECT *,
       stockout_months * 4 + low_stock_months * 2 + overstock_months AS priority_score
FROM inventory_summary
WHERE stockout_months >= 2
   OR low_stock_months >= 3
   OR overstock_months >= 3
ORDER BY priority_score DESC, avg_days_cover DESC;

-- 11. Revenue contribution by product (window function)
WITH product_sales AS (
    SELECT product_id, product_name, category, SUM(net_sales) AS revenue
    FROM sales
    GROUP BY product_id, product_name, category
)
SELECT
    *,
    revenue / SUM(revenue) OVER () AS revenue_share,
    SUM(revenue) OVER (ORDER BY revenue DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
      / SUM(revenue) OVER () AS cumulative_revenue_share
FROM product_sales
ORDER BY revenue DESC;

-- 12. Discount impact
SELECT
    discount_pct,
    COUNT(DISTINCT order_id) AS orders,
    SUM(net_sales) AS revenue,
    SUM(profit) AS profit,
    SUM(profit) / NULLIF(SUM(net_sales),0) AS margin_pct
FROM sales
GROUP BY discount_pct
ORDER BY discount_pct;
