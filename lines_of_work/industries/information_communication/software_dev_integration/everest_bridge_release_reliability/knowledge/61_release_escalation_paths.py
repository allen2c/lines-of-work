"""Release escalation paths for blocking issues."""

title = "Release Escalation Paths"

content = """
Escalation paths ensure that blocking issues during a release reach the right decision-makers
quickly. Define who to contact for different severity levels and when to escalate.

**Levels:** L1: Release engineer resolves. L2: Release Manager or team lead. L3: Release Board
or product owner. L4: Executive sponsor for go/no-go on critical releases.

**Triggers:** Escalate when gates fail repeatedly, when rollback is needed, when dependencies
block, or when stakeholder conflict arises. Document escalation in the release ticket.

**Response Times:** Define expected response windows (e.g. 15 min for L2 during deployment
window). Ensure on-call rotation covers release windows. Post escalation outcomes for learning.
"""

version = "0.0.1"
