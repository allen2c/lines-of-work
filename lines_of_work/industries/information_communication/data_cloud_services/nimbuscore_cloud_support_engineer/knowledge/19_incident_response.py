title = "Suspected Platform-Wide Incident Response"

content = """
- Indicators of a platform incident: a sharp non-uniform spike in tickets across multiple customers in the same region, matching log signatures, and an internal alert on the Status Dashboard.
- First action: check the Status Dashboard at `status.nimbuscore.internal`; if an incident is already open, link the customer ticket to it and use the holding language from the incident channel.
- If you suspect an incident that is not yet declared, page the Incident Commander on-call via PagerNC; do not wait for confirmation.
- Customer-facing language during an open incident must not speculate on root cause; refer to the public status page for updates.
- Document every customer touched during the incident in the incident ticket so the postmortem can account for impact.
"""  # noqa: E501

version = "0.0.1"
