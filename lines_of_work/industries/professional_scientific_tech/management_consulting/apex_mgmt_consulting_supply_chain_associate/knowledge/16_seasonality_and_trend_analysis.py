title = "Seasonality and Trend Analysis"

content = """
- Decompose time series into trend, seasonal, and residual components using moving average or STL (Seasonal-Trend decomposition using Loess).
- Example: retail demand shows strong yearly seasonality with peak in December (factor 1.5x average) and trough in February (0.7x). Use seasonal indices: December index = 1.5, February = 0.7.
- Trend: linear or exponential. If trend is positive (e.g., 5% growth per year), incorporate into forecast. Use Holt-Winters or regression with time variable.
- Residual: check for patterns (e.g., autocorrelation) to improve model. If residual has significant autocorrelation, consider ARIMA.
"""  # noqa: E501

version = "0.0.1"
