title = "Zero Downtime Deployment"

content = """
Zero downtime: deploy không affect user. Requirement cho production. Mekong
Delta Tech achieve zero downtime. Integration không interrupt.

**Strategy:** Rolling update. Blue-green. Canary. Multiple instance. Health
check. Drain. New instance ready. Switch. Old drain. No request drop. Session?
Sticky. Or stateless. Design for it.

**Database:** Migration backward compatible. Expand-contract. No destructive
change in single deploy. Both version work. Feature flag. Gradual. Plan.
Test. Rollback plan.

**Verification:** Smoke test post deploy. Health. Canary metric. Gradual
traffic. Monitor. Rollback trigger. Automated. Manual override. Document.
Drill. Confidence.
"""  # noqa: E501

version = "0.0.1"
