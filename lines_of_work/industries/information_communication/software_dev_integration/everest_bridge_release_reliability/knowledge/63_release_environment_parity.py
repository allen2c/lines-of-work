"""Release environment parity to reduce production surprises."""

title = "Release Environment Parity"

content = """
Environment parity means staging and pre-production closely match production in configuration,
data shape, and infrastructure. Parity reduces the risk of release failures caused by
environment-specific differences.

**Configuration:** Use the same configuration management approach across environments. Avoid
hardcoded environment-specific values. Use feature flags or environment variables for
differences that must exist (e.g. external API endpoints).

**Data:** Staging should use production-like data volumes and schemas where possible.
Anonymised production copies or synthetic data that mirrors production shape improve
realistic testing. Document known parity gaps.

**Infrastructure:** Match OS versions, runtime versions, and key infrastructure components.
Container images and base layers should be identical. Track drift and schedule parity reviews.
"""

version = "0.0.1"
