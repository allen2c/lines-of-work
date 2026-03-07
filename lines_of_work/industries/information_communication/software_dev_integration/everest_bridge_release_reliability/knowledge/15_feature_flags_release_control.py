"""Feature flags and release control knowledge item."""

title = "Feature Flags and Release Control"

content = """
Feature flags decouple deployment from feature activation. Code is deployed to production
while features remain disabled until explicitly enabled. This reduces release risk and
enables gradual rollout.

**Flag Lifecycle:** Define lifecycle stages: created, enabled in staging, enabled in
production (canary), fully rolled out, deprecated, removed. Track flags in a central
registry with owners and documentation.

**Release Strategy:** Use flags to ship incomplete or high-risk features behind a switch.
Deploy the code, verify in production with the flag off, then enable for a subset of
users or traffic. Roll back by disabling the flag without redeploying.

**Configuration Management:** Store flag state in a configuration system that supports
runtime changes. Avoid redeployments for flag toggles. Ensure flag state is consistent
across instances.

**Cleanup:** Remove flags after features are fully rolled out. Unused flags accumulate
technical debt and confusion. Schedule flag removal in the same release or the next.

**Audit:** Log flag changes with timestamp and actor. Support compliance and incident
investigation.
"""

version = "0.0.1"
