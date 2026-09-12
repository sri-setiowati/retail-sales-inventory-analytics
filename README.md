# Retail Sales & Inventory Analytics

End-to-end data analytics project focused on retail sales performance, profitability, product performance, and inventory risk.

This project demonstrates how sales and inventory data can be transformed into actionable business insights using **Python, SQL, Excel, and Power BI**.

> **Dataset Note:**  
> This project uses a fully synthetic dataset created for portfolio demonstration. The dataset is designed to simulate realistic retail sales and inventory scenarios and does not represent the performance of a real company.

---

## Business Problem

Retail businesses need to balance revenue growth, profitability, and inventory availability.

High sales do not necessarily mean high profitability, while excess inventory can tie up working capital and stockouts can result in missed sales opportunities.

This project analyzes retail transaction and inventory data to answer questions such as:

- Which product categories generate the most revenue and profit?
- Which categories have the strongest profit margins?
- Which products contribute most to overall revenue?
- Where are potential inventory risks occurring?
- Which products may require replenishment attention?
- Which products or categories may require further commercial review?
- What actions could management take based on the analysis?

---

## Project Objectives

The main objectives are to:

1. Analyze overall sales and profitability performance.
2. Identify high-performing products and categories.
3. Evaluate profit margins across product categories.
4. Identify inventory risks including stockout, low-stock, and overstock conditions.
5. Prioritize products requiring inventory attention.
6. Translate analytical findings into actionable business recommendations.
7. Demonstrate an end-to-end analytics workflow from raw data to business dashboard.

---

## Dataset

The project uses synthetic retail data designed to represent a small-to-medium retail environment.

### Main datasets

| Dataset | Description |
|---|---|
| `sales.csv` | Retail sales transactions |
| `products.csv` | Product master data |
| `inventory_snapshot.csv` | Inventory status and stock-related metrics |

The dataset contains information related to:

- Orders
- Products
- Categories
- Sales
- Costs
- Profit
- Quantity sold
- Inventory levels
- Stockout conditions
- Low-stock conditions
- Overstock conditions

---

## Analytical Workflow

The project follows an end-to-end analytical workflow:

```text
Raw Data
   ↓
Data Preparation
   ↓
Exploratory Data Analysis
   ↓
SQL Analysis
   ↓
Business Metrics
   ↓
Power BI Data Model
   ↓
DAX Measures
   ↓
Interactive Dashboard
   ↓
Business Insights
   ↓
Recommendations
Tools & Technologies
Python
Pandas
NumPy
Data cleaning
Data transformation
Exploratory data analysis
SQL
SELECT
WHERE
GROUP BY
JOIN
CASE WHEN
Aggregations
Business-oriented analytical queries
Power BI
Data modeling
Relationships
DAX measures
KPI cards
Interactive slicers
Sales analysis
Profitability analysis
Inventory risk analysis
Excel
Summary analysis
Category performance
Product performance
Inventory risk analysis
Data dictionary
Key Business Metrics

The analysis focuses on several core retail KPIs:

Total Revenue
Total Cost
Total Profit
Profit Margin
Total Orders
Units Sold
Average Order Value
Inventory Value
Low-Stock Products
Stockout Products
Overstock Products
Key Findings
Sales & Profitability

The analysis shows that Electronics is the largest revenue-generating category, while Sports demonstrates the strongest profit margin among the analyzed categories.

This highlights an important business distinction:

The category generating the most revenue is not necessarily the category generating the strongest margin.

This suggests that management should evaluate both revenue contribution and profitability when prioritizing products and categories.

Inventory

The inventory analysis identifies products exposed to different levels of inventory risk, including:

Stockout risk
Low-stock risk
Overstock risk

A priority-based approach can help management focus attention on products where inventory conditions may have the greatest potential business impact.

Business Recommendations

Based on the analysis, several actions can be considered:

1. Prioritize high-risk inventory

Review products with repeated stockout or low-stock conditions and evaluate whether replenishment policies need adjustment.

2. Review overstocked products

Identify products with consistently high inventory relative to sales activity and consider:

Promotional campaigns
Bundling
Pricing adjustments
Reduced replenishment quantities
3. Protect high-margin categories

Categories with stronger margins should be evaluated for opportunities to increase sales volume while maintaining profitability.

4. Review high-revenue but lower-margin products

High sales volume alone should not determine product priority. Products generating significant revenue but weaker margins may require pricing, sourcing, or product-mix review.

5. Improve inventory planning

A production version of this analysis could incorporate supplier lead times, purchase orders, historical demand patterns, and promotional calendars to improve replenishment decisions.

Dashboard

The Power BI dashboard is structured into two analytical views.

Sales & Profitability Overview

The first dashboard focuses on:

Revenue
Profit
Profit Margin
Orders
Units Sold
Average Order Value
Revenue trends
Category performance
Top products
Inventory Risk & Product Performance

The second dashboard focuses on:

Inventory value
Low-stock products
Stockout products
Overstock products
Inventory risk distribution
Product-level inventory priorities

Dashboard screenshots are available in the screenshots directory.

The Power BI source file is available in the powerbi directory.

Project Structure
retail-sales-inventory-analytics/
│
├── analysis/
│   └── ...
│
├── data/
│   ├── raw/
│   │   ├── sales.csv
│   │   ├── products.csv
│   │   └── inventory_snapshot.csv
│   │
│   └── processed/
│       └── ...
│
├── python/
│   └── ...
│
├── sql/
│   └── analysis_queries.sql
│
├── powerbi/
│   └── Retail_Sales_Inventory_Analytics.pbix
│
├── screenshots/
│   ├── dashboard_sales_overview.png
│   └── dashboard_inventory_analysis.png
│
├── docs/
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
Data Preparation

The Python pipeline is used to prepare the raw datasets before analysis.

Key preparation activities include:

Data type validation
Data cleaning
Missing-value checks
Duplicate checks
Feature preparation
Derived analytical fields
Exporting processed datasets

The main preparation script is available in:

python/data_preparation.py
SQL Analysis

SQL is used to answer business questions related to:

Sales performance
Product performance
Category performance
Profitability
Inventory risk

The analytical queries are available in:

sql/analysis_queries.sql
Power BI Data Model

The Power BI model uses a product dimension connected to sales and inventory data.

Conceptually:

             Products
            /        \
           /          \
          ↓            ↓
       Sales      Inventory

This structure allows product and category attributes to be used consistently across sales and inventory analysis.

Limitations

This project is intentionally designed as a portfolio demonstration and therefore has several limitations:

The dataset is synthetic.
The available time period is limited.
Inventory data represents snapshots rather than a complete daily inventory history.
Supplier lead times and purchase order history are not included.
Promotion and campaign data is limited.
The project focuses primarily on descriptive and diagnostic analytics rather than advanced demand forecasting.

A production implementation could be extended with:

Supplier lead times
Purchase orders
Historical inventory movements
Promotion and discount history
Customer-level data
Demand forecasting
Automated replenishment recommendations
Future Improvements

Potential future improvements include:

Demand forecasting
Inventory turnover analysis
Safety stock calculation
Reorder point optimization
Supplier performance analysis
Customer segmentation
Automated reporting
Power BI Service deployment
Scheduled data refresh
Disclaimer

This project is created for educational and portfolio demonstration purposes.

All business data is synthetic and should not be interpreted as representing an actual company's financial or operational performance.
