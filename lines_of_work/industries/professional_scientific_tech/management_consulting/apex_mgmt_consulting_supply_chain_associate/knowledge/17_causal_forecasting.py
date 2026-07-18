title = "Causal Forecasting"

content = """
- Use external variables that influence demand: price, promotions, advertising spend, competitor activity, weather, economic indicators (GDP, consumer confidence).
- Build multiple linear regression: Demand = β0 + β1*Price + β2*Promo + β3*GDP + ε. Example: Demand = 1000 - 20*Price + 500*Promo (dummy) + 0.1*GDP. R-squared >0.7 indicates good fit.
- Check assumptions: linearity, independence of errors, homoscedasticity, no multicollinearity (VIF <5). Use p-values (<0.05) to select significant variables.
- Forecast with predicted values of causal variables (e.g., planned promo spend, forecasted GDP). Update model quarterly.
"""  # noqa: E501

version = "0.0.1"
