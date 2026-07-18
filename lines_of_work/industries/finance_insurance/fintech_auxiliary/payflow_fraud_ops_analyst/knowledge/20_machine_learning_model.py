title = "Machine Learning Model Scores"

content = """
- Model is gradient boosting trained on historical fraud and legitimate transactions. Outputs risk score 0-100.
- Features: transaction amount, velocity, device age, IP reputation, user history, time since account creation.
- Model retrained monthly; performance monitored via AUC (target >0.95) and false positive rate.
- Analysts can override model score if evidence contradicts (e.g., known legitimate customer with high score due to travel).
"""  # noqa: E501

version = "0.0.1"
