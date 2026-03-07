"""Deployment approval chain for controlled releases."""

title = "Deployment Approval Chain"

content = """
The approval chain defines who must sign off before a release proceeds. Balance control
with speed; avoid unnecessary bottlenecks.

**Roles:** Typical roles include tech lead (technical readiness), product owner (scope
acceptance), and operations (production readiness). For critical services, add security
or compliance. Document who approves what and escalation path.

**Timing:** Request approvals before the deployment window. Use async approval where
possible; avoid blocking on real-time availability. Set clear deadlines.

**Audit:** Log all approvals with timestamp and approver. Store in release ticket or
audit system. Retain for compliance and post-incident review.
"""

version = "0.0.1"
