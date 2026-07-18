title = "Security Incident Handling"

content = """
- Suspected security indicators: leaked access keys in public repos, anomalous API calls from unfamiliar IPs, ransomware-style encryption of customer data, or reported breach by a third party.
- First action: do not attempt to remediate the customer's environment yourself; that is the customer's responsibility.
- Open a Security ticket with the `SEC-IR` queue and page Security Response on-call via PagerNC with severity `SEC-1` if data exfiltration is confirmed or suspected.
- Continue to engage the customer with status updates every 30 minutes until Security takes over; do not share internal investigation details.
- After handoff, the security pod owns all communication regarding the security aspect; you may still handle non-security follow-ups on the same ticket.
"""  # noqa: E501

version = "0.0.1"
