"""Release stakeholder approval workflow."""

title = "Release Stakeholder Approval"

content = """
Stakeholder approval ensures that releases align with business expectations and that key parties
have signed off before deployment. Define who must approve for each release type (e.g. product,
security, compliance) and what they are approving.

**Approval Matrix:** Map release types to required approvers. Standard releases may need product
and engineering sign-off. Releases touching regulated data need compliance. Security-sensitive
changes need security review. Document the matrix in the release process.

**Timing:** Request approvals early enough to avoid last-minute blocks. Use async approval
workflows where possible. Escalate stalled approvals per defined SLA.

**Audit:** Record approval timestamps, approver identity, and scope approved. Store in release
audit trail for compliance and post-incident review.
"""

version = "0.0.1"
