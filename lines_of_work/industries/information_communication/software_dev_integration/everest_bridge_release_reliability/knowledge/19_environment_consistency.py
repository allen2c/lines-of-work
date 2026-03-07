"""Environment consistency knowledge item."""

title = "Environment Consistency"

content = """
Environment consistency means staging and production are as similar as possible in
configuration, topology, and behavior. Divergence causes defects that appear only
in production.

**Infrastructure Parity:** Use the same infrastructure patterns: container orchestration,
load balancing, networking. Differences in scale are acceptable; differences in
architecture are not.

**Configuration Management:** Store configuration in version control. Use environment
variables or config services to vary only what must differ (e.g., endpoints, secrets).
Avoid manual configuration drift.

**Data:** Staging data should resemble production in structure and volume where
practical. Use anonymized production snapshots or synthetic data. Document data
differences and their impact on testing.

**Dependencies:** Staging should use the same external service versions and
configurations as production, or clearly documented substitutes. Integration tests
must run against representative dependencies.

**Validation:** Periodically audit environment parity. Automated checks can compare
configurations and topology. Address drift before it causes production incidents.
"""

version = "0.0.1"
