title = "Runbook Execution Guidelines"

content = """
- All runbooks are stored in a Git repository (runbooks.aetherdata.io) and version-controlled.
- For each alert type, the runbook is linked in the PagerDuty alert details.
- Runbooks include: symptoms, possible causes, step-by-step troubleshooting, mitigation commands, and rollback procedures.
- If a runbook step fails, note the failure in the incident timeline and try the next step. Do not skip steps.
- After incident, if the runbook was inaccurate or missing, create a Jira ticket in the "Runbooks" project with label `runbook-improvement`.
- Runbooks are tested quarterly during chaos engineering drills.
"""  # noqa: E501

version = "0.0.1"
