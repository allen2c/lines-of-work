title = "Automated Remediation Scripts"

content = """
- Several common issues have automated remediation scripts (e.g., restarting a stuck process, clearing a full disk, rebalancing partitions).
- Scripts are stored in the `automation` directory of the runbook repository. They are triggered via Slack commands (e.g., `/restart-service <service>`).
- Before running an automated script, verify that it matches the alert symptoms. Do not run blindly.
- After running, monitor the service for 5 minutes. If the issue persists, proceed with manual troubleshooting.
- All automated actions are logged in the incident timeline.
"""  # noqa: E501

version = "0.0.1"
