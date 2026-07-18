title = "Incident Response Matrix"

content = """
- SEV1: full outage of one or more P1 clusters, or any data loss. Page primary plus secondary DBA plus platform SRE. War room within 10 min. Status page update within 15 min.
- SEV2: partial degradation (replication lag above 60 s for more than 10 min, replica down for more than 15 min, backup failure for 2 consecutive cycles). Page primary DBA, Slack secondary.
- SEV3: minor degradation, single-node issue, non-P1 cluster affected. Ticket queue, 4 h response.
- SEV4: question, request, documentation gap. 1 business day.
- Post-mortem mandatory for SEV1 and SEV2 within 5 business days; action items tracked in dba-actions repo with owner and due date.
"""  # noqa: E501

version = "0.0.1"
