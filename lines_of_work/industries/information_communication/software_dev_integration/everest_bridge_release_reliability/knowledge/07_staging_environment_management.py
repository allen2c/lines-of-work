"""Staging environment management knowledge item."""

title = "Staging Environment Management"

content = """
Staging mirrors production as closely as possible to validate releases before deployment.
Environment parity reduces production surprises and builds confidence in the release.

**Parity Goals:** Match production in topology, configuration, and data shape. Use the
same deployment mechanism and similar scale where feasible. Document and justify any
intentional differences.

**Data Management:** Staging data should be representative but not production data.
Use anonymized copies, synthetic data, or subset loads. Refresh periodically to stay
aligned with schema and usage patterns.

**Availability:** Staging should be available for testing during release windows. Define
ownership, maintenance windows, and escalation when staging is unavailable.
"""

version = "0.0.1"
