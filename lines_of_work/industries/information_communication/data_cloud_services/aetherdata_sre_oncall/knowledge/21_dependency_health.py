title = "Dependency Health Monitoring"

content = """
- External dependencies: cloud APIs, DNS providers, CDN, monitoring tools (Datadog, PagerDuty), and third-party SaaS.
- Dependency health is shown on the Dependency Dashboard in Grafana, with status indicators (green/red).
- If a dependency is degraded, check its status page. If it’s a critical dependency (e.g., DNS), have a fallback plan.
- For dependencies that are down, open a support ticket and post in #incidents. Do not spend time troubleshooting their systems.
- After dependency recovers, verify that our services are reconnected and healthy.
"""  # noqa: E501

version = "0.0.1"
