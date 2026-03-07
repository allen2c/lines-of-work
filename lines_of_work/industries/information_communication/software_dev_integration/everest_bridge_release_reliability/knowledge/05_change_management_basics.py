"""Change management basics knowledge item."""

title = "Change Management Basics"

content = """
Change management provides structure and approval for modifications to production systems.
It balances speed of delivery with risk control and auditability.

**Change Types:** Classify changes by risk: standard (pre-approved, low risk), normal
(requires review and approval), and emergency (expedited for critical fixes). Each type
has defined approval paths and documentation requirements.

**Documentation:** Record what is changing, why, when, who approved it, and the rollback
plan. Link changes to tickets, release notes, and runbooks. This creates an audit trail
for compliance and post-incident analysis.

**Review and Approval:** Changes that affect production should be reviewed by someone
other than the implementer. Approval authority scales with risk. Emergency changes may
require post-implementation review.
"""

version = "0.0.1"
