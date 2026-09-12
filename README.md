Retail Sales & Inventory Analytics

End-to-end Data Analyst portfolio project combining SQL, Python (Pandas), and Power BI to answer a practical retail question: where is the business making money, and where is inventory creating risk?

Note on data: the dataset used in this project is synthetic, generated to resemble a realistic multi-category retail business. It is not real transaction data from a real company. The goal of this project is to demonstrate the analysis workflow — SQL, Python, data modeling, and Power BI — end to end.

Business Problem

A multi-channel retailer wants to understand revenue and profit performance while reducing inventory risk. This project looks at:

Revenue and profit trends by category
Channel and regional performance
Low-margin categories and discount impact
Stockout and overstock risk at the SKU level
Where replenishment and pricing attention should go first
Key Findings
Electronics drives the most revenue, contributing 37.3% of total revenue — the single largest category, ahead of Office, Home & Kitchen, Sports, and Beauty.
Beauty has the lowest margin of any category (23.1%), despite not being the smallest by revenue — worth a pricing and discount review before scaling it further.
Inventory risk is heavily skewed toward overstock, not stockout. At the SKU level, 65 items are in overstock versus only 8 in stockout — out of 3,200 orders and $2.75M in inventory value. The business is tying up far more capital in excess stock than it's losing in missed sales from empty shelves.
Overall: $301.3K revenue, $86.0K profit, ~28.5% gross margin across 3,200 orders.
Business Recommendations
Rebalance replenishment priorities toward overstock, not stockout — with 65 overstock items against 8 stockout items, the bigger opportunity is freeing up working capital tied up in slow-moving inventory, not preventing lost sales.
Review Beauty's pricing and discount strategy — its margin is the lowest of any category even though it isn't the lowest-revenue category, suggesting discounting or cost issues specific to that line.
Protect and grow Electronics as the primary revenue driver, while monitoring its margin closely since high-revenue categories can mask margin erosion if discounting increases over time.
Tools

Python (Pandas), SQL, Power BI, Excel

Files
python/ — data preparation and cleaning pipeline
sql/ — KPI, category performance, and inventory-risk queries
data/ — raw and processed datasets (synthetic)
analysis/ — exploratory analysis
screenshots/ — Power BI dashboard views
Dataset Scale

3,200 sales transactions · 65 products · 780 product-month inventory snapshots · Jan–Dec 2025 (synthetic)
