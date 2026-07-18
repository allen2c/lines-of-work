title = "Canary Deployment Process"

content = """
- All production deployments go through a canary phase: 5% of traffic for 10 minutes, then 25% for 10 minutes, then 100%.
- If error rate increases by > 1% or latency by > 10% during canary, the deployment is automatically rolled back.
- The on-call SRE monitors the canary dashboard during the deployment window. If an alert fires, follow the rollback procedure.
- Canary deployments are only allowed when error budget > 20%. Otherwise, use a manual deployment with senior approval.
"""  # noqa: E501

version = "0.0.1"
