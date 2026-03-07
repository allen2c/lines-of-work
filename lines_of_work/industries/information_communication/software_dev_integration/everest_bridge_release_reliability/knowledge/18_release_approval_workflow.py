"""Release approval workflow knowledge item."""

title = "Release Approval Workflow"

content = """
The approval workflow ensures that releases meet quality and business criteria before
deployment. It balances control with speed.

**Approvers:** Define who must approve: tech lead, product owner, release manager, or
compliance officer, depending on risk. Document approval authority in a RACI matrix.

**Criteria:** Approvers evaluate against documented criteria: tests passed, security
scan clean, documentation updated, stakeholder sign-off. Criteria are objective and
verifiable where possible.

**Escalation:** If approval is blocked, define escalation paths. Time-sensitive
releases may require expedited review. Document exceptions and their rationale.

**Audit:** Record approval decisions with timestamp, approver, and outcome. Support
compliance and post-incident review.

**Automation:** Automate approval for low-risk releases when criteria are met. Reserve
manual approval for high-risk or regulated changes. Reduce approval latency for
routine releases.
"""

version = "0.0.1"
