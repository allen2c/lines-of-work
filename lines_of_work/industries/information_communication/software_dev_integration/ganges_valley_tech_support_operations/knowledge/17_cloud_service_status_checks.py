title = "Cloud Service Status and Outage Awareness"

content = """
Modern software often depends on cloud providers (AWS, Azure, GCP) and third-party
APIs. Outages upstream can cause downstream issues. Check status before deep
troubleshooting.

**Status Pages:** Bookmark and routinely check provider status pages. Include
links in responses when an outage is suspected.

**Incident Correlation:** Multiple similar tickets in a short window may indicate
a platform incident. Report patterns to the incident response team.

**Customer Communication:** When an outage is confirmed, use templated messages
with ETA and workarounds when available. Avoid speculation on root cause.
"""  # noqa: E501

version = "0.0.1"
