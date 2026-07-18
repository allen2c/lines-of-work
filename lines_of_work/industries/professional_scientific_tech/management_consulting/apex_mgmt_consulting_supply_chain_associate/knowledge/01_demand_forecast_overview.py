title = "Demand Forecasting Overview"

content = """
- Types: qualitative (market research, Delphi method, expert judgment) and quantitative (time series, causal models). Time series methods include moving average, exponential smoothing (simple, Holt, Holt-Winters), and ARIMA. Causal models use regression with external drivers (e.g., price, promotions, GDP).
- Forecast horizon: short-term (1-3 months) for operational planning, medium-term (3-12 months) for budgeting, long-term (1+ years) for strategic decisions.
- Data requirements: at least 24 months of historical sales data, cleaned for outliers, promotions, and one-time events. Use daily or weekly granularity for short-term, monthly for medium-term.
- Accuracy benchmark: MAPE <10% is excellent, 10-20% acceptable, >20% requires model improvement or data review.
"""  # noqa: E501

version = "0.0.1"
