title = "Incident Response Process"

content = """
- Acknowledge alert within 2 minutes via PagerDuty mobile app or desktop.
- For SEV1/2: immediately declare incident in #incidents using the `/incident declare` Slack command. Provide alert ID, service affected, and initial impact.
- For SEV3/4: acknowledge and assess; if impact grows, reclassify.
- Assign Incident Commander (IC) – default is the acknowledging SRE unless a senior takes over.
- IC creates a Zoom bridge and posts the link in #incidents.
- All responders join the bridge; IC delegates tasks (e.g., investigation, mitigation, comms).
- Every 30 minutes (SEV1) or 60 minutes (SEV2), IC posts a status update in #incidents with current impact, actions taken, and ETA.
- After mitigation, IC declares incident resolved and starts the postmortem process.
"""  # noqa: E501

version = "0.0.1"
