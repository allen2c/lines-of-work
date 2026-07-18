title = "Demand Forecasting"

content = """
- Default model: D041 12-month rolling mean, with adjustments for known mission surges, fleet add-bys, and scheduled deployments.
- When fewer than 3 months of demand history exists, label the forecast as "indicative" and request the Provisioning team provide a curated demand model.
- Demand outliers: flag and remove any single month > 3 standard deviations from the rolling mean, then re-run; document the removal in the analyst's notebook.
- For seasonal items (e.g., cold-weather clothing, deployable shelters), apply the 24-month weighted mean to capture seasonality.
- Forecast accuracy KPI: target MAPE ≤ 25% for consumables, ≤ 40% for reparables in the first 12 months of service.
"""  # noqa: E501

version = "0.0.1"
