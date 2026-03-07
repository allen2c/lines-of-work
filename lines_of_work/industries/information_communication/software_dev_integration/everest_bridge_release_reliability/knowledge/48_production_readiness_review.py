"""Production readiness review checklist."""

title = "Production Readiness Review"

content = """
Before a release reaches production, conduct a production readiness review (PRR). This
ensures operational concerns are addressed: monitoring, runbooks, capacity, and rollback.

**Checklist Items:** Monitoring and alerting configured; runbooks updated; capacity
verified; dependencies and failover tested; rollback procedure documented and tested;
security and compliance checks passed; stakeholder sign-off obtained.

**Ownership:** The development team presents; operations and SRE review. Resolve or
accept risks before go-live. Document any deferred items with owners and timelines.

**Timing:** PRR should occur after staging validation, typically 1–2 days before
production deployment. For low-risk changes, a lightweight PRR may suffice.
"""

version = "0.0.1"
