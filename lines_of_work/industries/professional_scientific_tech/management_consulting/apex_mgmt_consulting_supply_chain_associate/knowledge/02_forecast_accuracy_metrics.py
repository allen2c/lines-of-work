title = "Forecast Accuracy Metrics"

content = """
- MAPE (Mean Absolute Percentage Error): average of |actual - forecast| / actual * 100. Use for comparing across products. Example: MAPE of 8% means average error is 8% of actual.
- MAE (Mean Absolute Error): average absolute difference. Useful when scale matters (e.g., units).
- RMSE (Root Mean Square Error): penalizes large errors more. RMSE = sqrt(mean of squared errors).
- Bias: average of (actual - forecast). Positive bias = under-forecast, negative = over-forecast. Acceptable bias range: -5% to +5% of mean demand.
- Tracking Signal (TS): cumulative error / MAD. If |TS| > 4, bias is significant and model needs adjustment.
"""  # noqa: E501

version = "0.0.1"
