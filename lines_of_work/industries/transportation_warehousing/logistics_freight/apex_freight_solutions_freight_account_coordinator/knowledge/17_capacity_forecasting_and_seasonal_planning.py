title = "Capacity Forecasting and Seasonal Planning"

content = """
- Forecast horizon: 13 weeks rolling; inputs: historical load volumes, customer sales forecasts, market capacity index (DAT Trendlines).  
- Model: ARIMA with exogenous variables (fuel price, produce season, retail calendar).  
- Output: required equipment count per lane per week; target 10 % buffer over forecast.  
- Action triggers: forecasted shortfall > 15 % → initiate spot market outreach, activate backup carriers, negotiate short‑term capacity contracts.  
- Review cycle: weekly forecast accuracy meeting (MAPE target ≤ 10 %).  
- Seasonal playbooks: Produce (Mar‑Jul), Holiday (Nov‑Dec), Back‑to‑School (Aug‑Sep).
"""  # noqa: E501

version = "0.0.1"
