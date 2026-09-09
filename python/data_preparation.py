"""Retail Sales & Inventory Analytics - data preparation pipeline.

Run from the repository root:
    python python/data_preparation.py

Inputs: data/raw/*.csv
Outputs: data/processed/*.csv and kpis.json/key_insights.txt
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

sales = pd.read_csv(RAW / "sales.csv", parse_dates=["order_date"])
products = pd.read_csv(RAW / "products.csv")
inventory = pd.read_csv(RAW / "inventory_snapshot.csv", parse_dates=["snapshot_date"])

# Validation
required_sales = {"order_id", "order_date", "product_id", "quantity", "net_sales", "cost", "profit"}
missing = required_sales - set(sales.columns)
if missing:
    raise ValueError(f"sales.csv missing columns: {sorted(missing)}")
if sales.duplicated("order_id").any():
    raise ValueError("Duplicate order_id values found.")
if (sales["quantity"] <= 0).any():
    raise ValueError("Sales quantity must be positive.")

# Feature engineering
sales["month"] = sales["order_date"].dt.to_period("M").astype(str)
sales["week"] = sales["order_date"].dt.to_period("W").astype(str)
sales["margin_pct"] = np.where(sales["net_sales"] != 0, sales["profit"] / sales["net_sales"], 0)

monthly = sales.groupby("month", as_index=False).agg(
    revenue=("net_sales", "sum"),
    profit=("profit", "sum"),
    orders=("order_id", "nunique"),
    units_sold=("quantity", "sum"),
)
monthly["margin_pct"] = monthly["profit"] / monthly["revenue"]
monthly.to_csv(PROC / "monthly_sales.csv", index=False)

weekly = sales.groupby("week", as_index=False).agg(
    revenue=("net_sales", "sum"), profit=("profit", "sum"),
    orders=("order_id", "nunique"), units_sold=("quantity", "sum")
)
weekly["margin_pct"] = weekly["profit"] / weekly["revenue"]
weekly.to_csv(PROC / "weekly_sales.csv", index=False)

product_perf = sales.groupby(["product_id", "product_name", "category"], as_index=False).agg(
    revenue=("net_sales", "sum"), profit=("profit", "sum"),
    units_sold=("quantity", "sum"), orders=("order_id", "nunique")
)
product_perf["margin_pct"] = product_perf["profit"] / product_perf["revenue"]
product_perf = product_perf.sort_values("revenue", ascending=False)
product_perf.to_csv(PROC / "product_performance.csv", index=False)

category_perf = sales.groupby("category", as_index=False).agg(
    revenue=("net_sales", "sum"), profit=("profit", "sum"),
    units_sold=("quantity", "sum"), orders=("order_id", "nunique")
)
category_perf["margin_pct"] = category_perf["profit"] / category_perf["revenue"]
category_perf["revenue_share"] = category_perf["revenue"] / category_perf["revenue"].sum()
category_perf = category_perf.sort_values("revenue", ascending=False)
category_perf.to_csv(PROC / "category_performance.csv", index=False)

inventory_risk = inventory.groupby(
    ["product_id", "product_name", "category", "supplier", "reorder_point"], as_index=False
).agg(
    avg_days_cover=("days_of_cover", "mean"),
    min_closing_stock=("closing_stock", "min"),
    avg_closing_stock=("closing_stock", "mean"),
    months_stockout=("stock_status", lambda s: int((s == "Stockout").sum())),
    months_low_stock=("stock_status", lambda s: int((s == "Low Stock").sum())),
    months_overstock=("stock_status", lambda s: int((s == "Overstock").sum())),
)
inventory_risk["risk_flag"] = np.select(
    [inventory_risk["months_stockout"] >= 2,
     inventory_risk["months_low_stock"] >= 3,
     inventory_risk["months_overstock"] >= 3],
    ["High Stockout Risk", "Watch Low Stock", "Overstock Risk"],
    default="Normal",
)
inventory_risk["priority_score"] = (
    inventory_risk["months_stockout"] * 4
    + inventory_risk["months_low_stock"] * 2
    + inventory_risk["months_overstock"]
)
inventory_risk = inventory_risk.sort_values(
    ["priority_score", "months_stockout", "avg_days_cover"], ascending=[False, False, False]
)
inventory_risk.to_csv(PROC / "inventory_risk.csv", index=False)

# Power BI-friendly dimension exports
products.to_csv(PROC / "dim_products.csv", index=False)
inventory.to_csv(PROC / "inventory_snapshot_clean.csv", index=False)
sales.to_csv(PROC / "fact_sales_clean.csv", index=False)

kpis = {
    "total_revenue": round(float(sales["net_sales"].sum()), 2),
    "total_profit": round(float(sales["profit"].sum()), 2),
    "gross_margin_pct": round(float(sales["profit"].sum() / sales["net_sales"].sum()), 4),
    "orders": int(sales["order_id"].nunique()),
    "units_sold": int(sales["quantity"].sum()),
    "avg_order_value": round(float(sales["net_sales"].sum() / sales["order_id"].nunique()), 2),
    "products": int(products["product_id"].nunique()),
    "stockout_product_months": int((inventory["stock_status"] == "Stockout").sum()),
    "overstock_product_months": int((inventory["stock_status"] == "Overstock").sum()),
}
(PROC / "kpis.json").write_text(json.dumps(kpis, indent=2))

best_cat = category_perf.iloc[0]
worst_margin = category_perf.sort_values("margin_pct").iloc[0]
high_risk = inventory_risk[inventory_risk["risk_flag"] != "Normal"].head(5)
insights = [
    f"{best_cat['category']} is the largest revenue contributor at {best_cat['revenue_share']:.1%} of total revenue.",
    f"{worst_margin['category']} has the lowest category margin at {worst_margin['margin_pct']:.1%}; pricing and discounting should be reviewed.",
    f"{kpis['stockout_product_months']} product-month stockout observations were identified, creating availability risk.",
    f"{kpis['overstock_product_months']} product-month overstock observations were identified, indicating excess working-capital exposure.",
    "Prioritize products with repeated stockouts first, then review high-cover SKUs for purchase-order and replenishment adjustments.",
]
(PROC / "key_insights.txt").write_text("\n".join(insights))

print(json.dumps(kpis, indent=2))
print(f"Processed files written to {PROC}")
