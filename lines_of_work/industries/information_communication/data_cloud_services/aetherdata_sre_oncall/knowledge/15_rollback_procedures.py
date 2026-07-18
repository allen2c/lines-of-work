title = "Rollback Procedures"

content = """
- For SEV1/2 incidents caused by a recent deployment, rollback immediately using the automated script: `/rollback <service> <version>` in #deployments.
- The script will revert to the previous stable version and restart the service.
- After rollback, verify service health via the monitoring dashboard. If health does not improve within 5 minutes, escalate.
- For SEV3, assess impact first. If rollback is needed, coordinate with the deployment team.
- Document the rollback in the incident timeline, including the version rolled back and the reason.
"""  # noqa: E501

version = "0.0.1"
