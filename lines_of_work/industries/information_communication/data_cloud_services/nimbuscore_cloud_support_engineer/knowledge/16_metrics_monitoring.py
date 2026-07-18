title = "Metrics, Alarms, and Dashboards"

content = """
- Standard metric resolution is 1 minute; detailed monitoring is 1 minute with additional percentiles at additional cost.
- Alarms have three states: `OK`, `INSUFFICIENT_DATA`, `ALARM`. A persistent `INSUFFICIENT_DATA` is almost always a metric stream problem, not a workload problem.
- Composite alarms can combine up to 100 underlying alarms with AND/OR/NOT logic; use them for "all of these in the same AZ" patterns.
- For customer dashboards, never share a dashboard that contains another customer's resource IDs, even if redacted with a regex.
- When recommending an alarm, always specify the statistic (avg vs p99 vs max), the period (60s vs 300s), and the evaluation periods (3 of 5 is a common anti-flap rule).
"""  # noqa: E501

version = "0.0.1"
