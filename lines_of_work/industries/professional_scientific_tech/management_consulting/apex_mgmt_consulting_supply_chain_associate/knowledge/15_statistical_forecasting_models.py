title = "Statistical Forecasting Models"

content = """
- Exponential smoothing: simple (no trend/seasonality), Holt (trend), Holt-Winters (trend + seasonality). Parameters (alpha, beta, gamma) typically between 0.1 and 0.3. Example: Holt-Winters with alpha=0.2, beta=0.1, gamma=0.1 for monthly data with trend and 12-month seasonality.
- ARIMA: (p,d,q) where p=autoregressive, d=differencing, q=moving average. Use ACF/PACF plots to identify orders. Example: ARIMA(1,1,1) for non-stationary data with one lag each.
- Model selection: compare AIC or BIC; lower is better. For short-term forecasts, simpler models often outperform complex ones. Validate on holdout sample (last 3-6 months).
"""  # noqa: E501

version = "0.0.1"
