"""Deployment retry strategy for transient failures."""

title = "Deployment Retry Strategy"

content = """
Transient failures (network blips, temporary unavailability) can cause deployments to
fail unnecessarily. A retry strategy improves success rates while avoiding infinite
loops.

**Retry Policy:** Define max retries, backoff (linear or exponential), and conditions
for retry (e.g. only on 5xx, timeout). Do not retry on 4xx or deterministic failures.

**Idempotency:** Ensure deployment steps are idempotent so retries do not cause
duplicate or conflicting changes. Use conditional updates where applicable.

**Monitoring:** Log retry attempts and outcomes. Alert if max retries exceeded. Distinguish
transient vs. persistent failures for incident response.
"""

version = "0.0.1"
