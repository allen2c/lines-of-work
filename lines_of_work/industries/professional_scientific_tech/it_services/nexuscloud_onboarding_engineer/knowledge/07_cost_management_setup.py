title = "Cost Management Setup"

content = """
- Enable cost allocation tags: mandatory tags - `Customer`, `Environment`, `CostCenter`, `Project`. Engineer must apply to all resources.
- Set budget alerts: 80% and 100% of monthly budget. Notify customer via email and Slack. Budget defined in contract (e.g., $10,000/month for Standard).
- Use NexusCloud Cost Optimizer tool to identify idle resources (CPU <5% for 7 days). Generate weekly report.
- For Premium/Enterprise: set up anomaly detection (spend >20% above forecast). Auto-create ticket for review.
- Customer can request custom budget thresholds - must be approved by finance team.
"""

version = "0.0.1"
