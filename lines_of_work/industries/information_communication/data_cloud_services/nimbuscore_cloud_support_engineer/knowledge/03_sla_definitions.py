title = "SLA Targets, Measurement, and Breach Handling"

content = """
- Response SLA is measured from ticket creation to first human reply; resolution SLA is measured from creation to a customer-confirmed or engineer-marked "Resolved" state.
- Resolution targets by priority: Sev-1 = 4 hours, Sev-2 = 1 business day, Sev-3 = 3 business days, Sev-4 = 7 business days.
- "Business day" is defined as 09:00-18:00 in the customer's home region local time, Monday-Friday, excluding the customer's listed public holidays.
- An SLA breach is auto-flagged by the system at 90% of the target window; you must update the customer with a status note before the 100% mark.
- Breaches caused by NimbusCore-side issues (platform incident, staffing gap) are flagged with the "vendor_sla_breach" tag and excluded from individual CSAT scoring.
"""  # noqa: E501

version = "0.0.1"
