# Retail Sales & Inventory Analytics

End-to-end Data Analytics project analyzing retail sales performance, profitability, product performance, and inventory risk using Python, SQL, Excel, and Power BI.

The project demonstrates a complete analytical workflow — from data preparation and exploratory analysis to SQL analysis, business KPI development, interactive Power BI dashboards, and actionable business recommendations.

> **Dataset Note**
>
> This project uses a fully synthetic dataset created specifically for portfolio demonstration. The data is designed to simulate realistic retail sales and inventory scenarios and does not represent the performance or operations of a real company.

---

## 📌 Project Overview

Retail businesses need to balance revenue growth, profitability, and inventory availability.

A product may generate high revenue but relatively low profit, while another product may have strong margins but limited sales volume. At the same time, stockouts can lead to missed sales opportunities, while excess inventory can tie up working capital.

This project analyzes retail sales and inventory data to identify:

- Revenue and profit performance
- Category and product performance
- Profitability and margin differences
- High-performing products
- Low-margin products
- Stockout and low-stock risks
- Overstock conditions
- Products requiring inventory attention
- Business opportunities for pricing, product prioritization, and inventory management

---

# 🎯 Business Objectives

The main objectives of this project are to:

1. Evaluate overall sales and profitability performance.
2. Identify the strongest and weakest product categories.
3. Identify products contributing significantly to revenue and profit.
4. Analyze differences between revenue contribution and profitability.
5. Identify inventory risks at the product level.
6. Prioritize products requiring replenishment or inventory action.
7. Translate analytical findings into actionable business recommendations.
8. Demonstrate an end-to-end Data Analyst workflow using multiple analytical tools.

---

# ❓ Business Questions

The analysis focuses on several key business questions:

### Sales Performance

- How much revenue and profit did the business generate?
- How has revenue and profit changed over time?
- Which categories generate the most revenue?
- Which categories generate the most profit?
- Which products contribute the most revenue?

### Profitability

- Which categories have the strongest profit margins?
- Which categories generate high revenue but relatively lower margins?
- Which products contribute significantly to overall profitability?
- Where might pricing or product-mix optimization be required?

### Inventory

- Which products are experiencing stockout conditions?
- Which products are at low-stock risk?
- Which products are potentially overstocked?
- Which products should receive the highest inventory attention?
- Which inventory risks could potentially affect sales performance?

---

# 🗂️ Dataset

The project uses a synthetic retail dataset representing sales transactions, product information, and inventory conditions.

## Main Datasets

| Dataset | Description |
|---|---|
| `sales.csv` | Retail sales transaction data |
| `products.csv` | Product master data |
| `inventory_snapshot.csv` | Product-level inventory snapshot data |

### Dataset Scale

- **3,200** sales transactions/orders
- **65** products
- **780** inventory product-month snapshots
- Analysis period: **January–December 2025**

---

# 🔍 Data Contents

The datasets contain information related to:

### Sales

- Order ID
- Order date
- Product
- Category
- Quantity
- Revenue
- Cost
- Profit

### Products

- Product ID
- Product name
- Category
- Product attributes
- Pricing/cost information

### Inventory

- Product ID
- Inventory date/month
- Stock level
- Inventory condition
- Stockout indicators
- Low-stock indicators
- Overstock indicators
- Priority/risk metrics

---

# 🛠️ Tools & Technologies

## Python

Used for data preparation, cleaning, transformation, and analytical preprocessing.

Libraries:

- Pandas
- NumPy

Key activities:

- Data type validation
- Data cleaning
- Duplicate checks
- Missing-value checks
- Data transformation
- Feature preparation
- Processed dataset generation

---

## SQL

Used to answer business-oriented analytical questions and validate key metrics.

Techniques include:

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- JOIN
- CASE WHEN
- Aggregate functions
- Conditional analysis
- Product and category analysis

---

## Power BI

Used to build the analytical data model and interactive dashboards.

Key features:

- Data modeling
- Table relationships
- DAX measures
- KPI cards
- Interactive slicers
- Category analysis
- Product performance analysis
- Profitability analysis
- Inventory risk analysis

---

## Excel

Used as a supporting analytical and validation layer.

The analysis includes:

- Project summary
- Category performance
- Top products
- Inventory risk
- Data dictionary

---

## Git & GitHub

Used for:

- Version control
- Project organization
- Documentation
- Portfolio presentation
- Reproducibility

---

# 🔄 Analytical Workflow

The project follows an end-to-end Data Analytics workflow:

```text
Raw Data
    ↓
Data Preparation
    ↓
Data Cleaning & Validation
    ↓
Exploratory Data Analysis
    ↓
SQL Business Analysis
    ↓
KPI Development
    ↓
Power BI Data Modeling
    ↓
DAX Measures
    ↓
Interactive Dashboard
    ↓
Business Insights
    ↓
Recommendations
🧹 Data Preparation

The raw datasets were processed using Python/Pandas before being used for analysis.

The preparation workflow includes:

Data type validation
Missing-value checks
Duplicate checks
Data consistency checks
Data transformation
Derived analytical fields
Processed dataset generation

The main preparation script is available in:

python/data_preparation.py
📊 Exploratory & Business Analysis

The analysis focuses on four major areas:

1. Sales Performance

Analyze revenue, orders, units sold, and sales trends.

2. Profitability

Evaluate cost, profit, and profit margins across products and categories.

3. Product Performance

Identify high-performing and underperforming products based on revenue and profitability.

4. Inventory Risk

Identify products exposed to:

Stockout
Low-stock
Overstock

and prioritize products requiring further attention.

🧮 Key Business Metrics

The project evaluates several core retail KPIs:

KPI	Purpose
Total Revenue	Measures overall sales value
Total Cost	Measures associated product cost
Total Profit	Measures gross profit contribution
Profit Margin %	Measures profitability relative to revenue
Total Orders	Measures transaction volume
Units Sold	Measures product demand volume
Average Order Value	Measures average revenue per order
Inventory Value	Measures capital tied to inventory
Low Stock Items	Identifies products requiring stock attention
Stockout Items	Identifies potential lost-sales risk
Overstock Items	Identifies excess inventory risk
📈 Power BI Dashboard

The Power BI dashboard is designed around two main analytical views.

Page 1 — Sales & Profitability Overview

The first dashboard provides an executive-level view of sales and profitability.

KPIs
Total Revenue
Total Profit
Profit Margin %
Total Orders
Units Sold
Average Order Value
Visual Analysis
Revenue and profit trend
Revenue by category
Profit by category
Revenue contribution by category
Top products by revenue
Category performance table
Interactive Filters
Date
Category
Product
Page 2 — Inventory Risk & Product Performance

The second dashboard focuses on inventory health and product-level risk.

KPIs
Inventory Value
Low Stock Items
Stockout Items
Overstock Items
At-Risk Products
Visual Analysis
Inventory risk distribution
Inventory by category
Product inventory risk
High-priority products
Stockout and low-stock conditions
Overstock analysis

The dashboard screenshots are available in:

screenshots/

The Power BI source file is available in:

powerbi/
🧩 Power BI Data Model

The Power BI model uses product information as a shared dimension for sales and inventory analysis.

Conceptually:

                  Products
                 /        \
                /          \
               ↓            ↓
             Sales      Inventory

The product table provides product and category attributes used across the sales and inventory analysis.

This structure helps maintain consistent filtering and analysis across the dashboard.

💡 Key Findings
Sales & Revenue

Electronics is the largest revenue-generating category in the analyzed dataset.

However, revenue leadership does not automatically translate into the strongest profitability.

This demonstrates why retail performance should be evaluated using both revenue and profit rather than sales volume alone.

Profitability

Sports shows the strongest profit margin among the analyzed categories.

This indicates that categories with lower absolute revenue can still generate attractive profitability.

From a management perspective, category prioritization should therefore consider:

Revenue contribution
Profit contribution
Profit margin
Sales volume

rather than relying on a single KPI.

Product Performance

Several products contribute significantly to overall revenue.

High-revenue products can become important commercial priorities because changes in pricing, availability, or demand can have a meaningful effect on overall business performance.

However, product prioritization should also consider profitability and inventory conditions.

Inventory Risk

The inventory analysis identifies multiple product-level risks, including:

Stockout
Low stock
Overstock

These conditions represent different business challenges.

Stockout

Potential risk of:

Lost sales
Customer dissatisfaction
Reduced product availability
Low Stock

Potential indication that replenishment may be required.

Overstock

Potential risk of:

Excess working capital
Higher holding costs
Slow-moving inventory
Increased markdown requirements
🎯 Business Recommendations

Based on the analysis, several actions can be considered.

1. Prioritize Stockout & Low-Stock Products

Products with repeated stockout or low-stock conditions should receive replenishment attention.

The business could review:

Historical sales
Current stock
Replenishment frequency
Supplier lead time
Safety stock requirements
2. Review Overstocked Products

Products with persistent excess inventory should be evaluated for possible inventory reduction.

Potential actions include:

Promotional campaigns
Bundling
Pricing adjustments
Reduced replenishment quantities
Clearance strategies
3. Protect High-Margin Categories

Categories with stronger profit margins may provide opportunities for profitable growth.

Management could evaluate:

Increasing sales volume
Expanding product assortment
Maintaining competitive pricing
Prioritizing high-margin products
4. Review High-Revenue but Lower-Margin Products

Products generating significant revenue but relatively lower profitability should be reviewed for:

Pricing optimization
Procurement cost reduction
Supplier negotiation
Product-mix optimization
Discount strategy
5. Improve Inventory Planning

A production implementation could combine sales history with:

Supplier lead time
Purchase orders
Historical inventory movements
Safety stock
Promotions
Demand forecasts

to improve replenishment decisions.

📁 Project Structure
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
│   ├── data_preparation.py
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
📦 Project Deliverables
Deliverable	Description
Raw datasets	Original synthetic retail datasets
Processed datasets	Cleaned and transformed datasets
Python pipeline	Data preparation and transformation
SQL analysis	Business-oriented analytical queries
Excel analysis	Supporting analysis and validation
Power BI dashboard	Interactive sales and inventory analysis
Dashboard screenshots	Portfolio dashboard previews
Documentation	Data dictionary and project methodology
📚 SQL Analysis

SQL is used to answer business questions related to:

Revenue performance
Profitability
Category performance
Product performance
Inventory risk
Product prioritization

The main SQL analysis file is:

sql/analysis_queries.sql
📓 Python Analysis

Python is used as the primary data preparation and analytical preprocessing tool.

The project uses Pandas and NumPy for:

Data cleaning
Data transformation
Validation
Feature preparation
Analytical dataset generation

Main script:

python/data_preparation.py
⚠️ Limitations

This project is intentionally designed as a portfolio demonstration and therefore has several limitations.

Synthetic Dataset

All business data is synthetic and does not represent an actual company's operational or financial performance.

Limited Time Period

The analysis covers a defined portfolio dataset rather than multiple years of historical business data.

Inventory Snapshots

Inventory information is based on product-month snapshots rather than a complete daily inventory movement history.

Missing Supplier Information

Supplier lead times, purchase orders, and supplier performance metrics are not included.

Limited Promotion Data

Detailed promotion and campaign history is not available.

Forecasting

The project focuses primarily on descriptive and diagnostic analytics rather than advanced demand forecasting.

🚀 Future Improvements

Potential extensions for a production-level implementation include:

Demand forecasting
Inventory turnover analysis
Safety stock calculation
Reorder point optimization
Supplier performance analysis
Customer segmentation
Promotion effectiveness analysis
Automated replenishment recommendations
Power BI Service deployment
Scheduled data refresh
Automated reporting
🧠 Skills Demonstrated

This project demonstrates practical experience in:

Data Cleaning
Data Preparation
Exploratory Data Analysis
Python / Pandas
SQL
KPI Development
Data Modeling
DAX
Power BI
Business Intelligence
Inventory Analytics
Profitability Analysis
Business Problem Solving
Data Visualization
Business Storytelling
Git & GitHub
📌 Conclusion

This project demonstrates how a Data Analyst can transform raw retail data into business-oriented insights.

Rather than focusing only on sales volume, the analysis combines:

Sales
+
Profitability
+
Product Performance
+
Inventory Risk

to provide a broader view of retail business performance.

The final workflow demonstrates the ability to move from raw data to analysis, visualization, and actionable recommendations using Python, SQL, Excel, and Power BI.

Disclaimer

This project is created for educational and portfolio demonstration purposes.

All datasets and business scenarios are synthetic and should not be interpreted as representing the actual performance, operations, customers, or financial results of a real company.
