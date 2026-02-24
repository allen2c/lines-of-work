title = "Fault Injection"

content = """
Fault injection test system behavior khi dependency fail. Proactive resilience
testing. Mekong Delta Tech dùng fault injection trong staging.

**Types:** Latency injection (delay response). Error injection (return 500).
Timeout. Connection reset. Partial failure. Chaos engineering.

**When:** Staging, pre-prod. Not production (unless canary, dark launch).
Controlled. Short duration. Specific target. Monitor impact.

**Goals:** Verify retry works. Circuit breaker trips. Fallback activates.
No cascade failure. Recovery correct. Find weakness before production.

**Tools:** Chaos Monkey, Toxiproxy, custom middleware. Feature flag to enable.
Admin-only. Audit log. Run as drill. Document learning.
"""  # noqa: E501

version = "0.0.1"
