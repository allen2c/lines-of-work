title = "Incident Response Procedures"

content = """
Incident response follows a structured lifecycle that ensures consistency,
traceability, and legal defensibility across all cyber events affecting the unit.

**Phase 1 — Preparation:** Maintain current playbooks for each high-likelihood incident
type (ransomware, credential compromise, data exfiltration, insider threat). Playbooks
are reviewed quarterly and updated after every significant incident. All responders hold
current incident handler qualifications.

**Phase 2 — Detection and Analysis:** Alerts originate from the SIEM, endpoint detection
and response (EDR) tools, user reports, or partner agency notifications. The on-duty
analyst triages each alert, assigns a priority (P1–P4), and determines whether the
event constitutes a confirmed incident. P1 (mission-critical impact) requires immediate
escalation to the shift supervisor regardless of time of day.

**Phase 3 — Containment:** Containment strategy depends on incident type. For active
intrusions, isolate affected hosts from the network while preserving volatile memory.
For insider threats, revoke credentials before notification to prevent evidence
destruction. Containment actions are logged with timestamps in the incident ticket.

**Phase 4 — Eradication:** Remove malicious artifacts (malware, unauthorized accounts,
persistence mechanisms) from all affected systems. Validate eradication by re-scanning
affected hosts with updated signatures. Do not return a system to production until a
clean scan is confirmed and documented.

**Phase 5 — Recovery:** Restore affected systems from a known-good backup or rebuild
from approved baseline images. Verify system integrity before reconnecting to the
enclave. Monitor recovered systems with elevated fidelity for 72 hours post-recovery.

**Phase 6 — Lessons Learned:** Conduct a post-incident review within five business days.
Document root cause, timeline, detection gaps, and corrective actions. Distribute a
sanitized incident report to relevant stakeholders at the appropriate classification.
"""

version = "0.0.1"
