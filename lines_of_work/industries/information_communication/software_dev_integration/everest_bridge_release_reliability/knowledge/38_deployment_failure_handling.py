"""Deployment failure handling knowledge item."""

title = "Deployment Failure Handling"

content = """
When a deployment fails, follow a defined procedure. Stop the pipeline; do not retry
automatically without investigation. Log failure context: stage, error, environment state.
Notify release owner and on-call. Determine root cause before retry. If partial deployment
occurred, assess rollback necessity. Document failure in postmortem. Update runbooks if
failure reveals process gaps.
"""

version = "0.0.1"
