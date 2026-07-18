title = "Forecast Bias Detection"

content = """
- Calculate cumulative forecast error (sum of actual - forecast over a period). If consistently positive, under-forecasting; if negative, over-forecasting.
- Tracking Signal (TS) = cumulative error / MAD. MAD = mean absolute deviation. TS > 4 or < -4 indicates bias. Example: cumulative error = +500, MAD = 100, TS = 5 → bias present.
- Bias percentage = (sum of errors / sum of actual) * 100. Acceptable range: -5% to +5%. If bias >5%, adjust forecast by adding bias correction factor (e.g., multiply forecast by 1.05 if under-forecasting).
- Investigate root cause: model misspecification, missing causal factors, or systematic over-optimism from sales team.
"""  # noqa: E501

version = "0.0.1"
