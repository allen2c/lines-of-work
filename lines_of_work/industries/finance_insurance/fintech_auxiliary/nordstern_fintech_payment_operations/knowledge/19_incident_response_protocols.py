title = "Incident Response Protocols"

content = """
Payment and system incidents require coordinated response. Operations
follow defined protocols for communication and escalation.

**Outage Classification:** Incidents are classified by severity: full
outage (no payments processing), partial degradation (specific payment
types or regions affected), or intermittent errors. Severity drives
communication cadence and escalation.

**Status Page:** Nordstern maintains a status page for real-time incident
visibility. Merchants should subscribe to updates. Do not rely solely
on support tickets for outage information during incidents.

**Communication:** During major incidents, we provide periodic updates
until resolution. Post-incident reports summarize root cause and
remediation. Affected merchants may receive direct notification
depending on impact.

**Merchant Actions During Outage:** Merchants should: avoid retrying
failed requests excessively (respect rate limits and backoff), inform
customers of payment delays, and capture orders for later processing
if business-critical. Do not switch to unverified or alternate
processing without prior approval.

**Security Incidents:** Suspected data breach or unauthorized access
must be reported immediately to the designated security contact.
"""  # noqa: E501

version = "0.0.1"
