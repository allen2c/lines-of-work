title = "Runbook Library Usage and Maintenance"

content = """
- The Runbook Library lives at `runbooks.nimbuscore.internal`. Each runbook has an owner, last-reviewed date, and version. Do not follow a runbook older than 12 months without flagging it for review.
- Standard runbook structure: Summary, Preconditions, Diagnostic Steps, Remediation, Verification, Escalation Criteria, Postmortem Hook.
- When a runbook step fails, stop, capture the exact output, and either adapt with a manager-approved deviation or escalate; do not improvise beyond the documented steps.
- After any confirmed root cause, file a runbook improvement ticket with the diff in markdown; the runbook squad triages weekly.
- Never edit a runbook directly from a customer ticket; that is a separate change-management workflow.
"""  # noqa: E501

version = "0.0.1"
