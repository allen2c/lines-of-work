title = "Ticket Intake, Triage, and Priority Assignment"

content = """
- T1 intake validates customer identity, contract status, and support entitlement before assigning to T1.5.
- At intake, confirm: affected service, affected region, affected resource IDs, business impact, and the earliest observable timestamp.
- Priority matrix: Sev-1 = production workload fully down, no workaround; Sev-2 = production degraded, workaround exists or limited scope; Sev-3 = non-production impact or single-feature degradation; Sev-4 = question, how-to, or cosmetic.
- Sev-1 must be acknowledged within 15 minutes and the on-call lead notified in the #sev1 channel within 20 minutes.
- If a ticket is misrouted (e.g., a billing question lands in T1.5), reassign within 10 minutes and do not start troubleshooting.
"""  # noqa: E501

version = "0.0.1"
