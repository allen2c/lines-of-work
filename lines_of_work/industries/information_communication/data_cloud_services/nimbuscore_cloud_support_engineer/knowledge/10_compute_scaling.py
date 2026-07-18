title = "Auto Scaling, Launch Templates, and Capacity Issues"

content = """
- Auto Scaling groups evaluate health every 30 seconds by default; an instance is replaced if unhealthy for 3 consecutive checks.
- Common ASG launch failures: AMI ID not available in the target region, IAM role missing `ec2:RunInstances`, subnet without enough free IPs (each subnet reserves 5 IPs).
- Predictive scaling requires at least 14 days of historical metrics; otherwise the group falls back to dynamic target tracking.
- Spot interruption notice gives a 2-minute warning; customers should architect for graceful shutdown within that window using the instance metadata `instance-action` endpoint.
- If a customer needs to freeze scaling for a black Friday event, recommend the `suspended` process flag rather than disabling the ASG entirely.
"""  # noqa: E501

version = "0.0.1"
