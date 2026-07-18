title = "Capacity Planning Procedures"

content = """
- Weekly review of capacity dashboards for all production clusters.
- If any resource (CPU, memory, disk, network) exceeds 80% utilization for 4 consecutive hours, file a capacity planning ticket in Jira (project CAP).
- Ticket must include: service name, resource type, current utilization, growth trend (last 30 days), and recommended action (scale up, scale out, or optimize).
- For sustained growth > 10% per month, escalate to the infrastructure team for long-term planning.
- Capacity planning is done quarterly with a formal review of all services.
"""  # noqa: E501

version = "0.0.1"
