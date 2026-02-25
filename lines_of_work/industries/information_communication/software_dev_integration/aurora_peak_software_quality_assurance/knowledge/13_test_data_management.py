title = "Test Data Management and Synthetic Data"

content = """
Quality testing requires realistic, consistent test data. We manage test
datasets to support automation, avoid PII exposure, and enable
reproducible scenarios.

**Synthetic Data:** We generate synthetic data for names, account numbers,
and transactions. Generators produce data that satisfies business rules
(e.g., valid account structures, date ranges) without using real
customer information.

**Data Refresh and Isolation:** Test environments are refreshed from
production snapshots (anonymized) or synthetic loads on a schedule.
Tests must not depend on shared mutable state that could cause
interference between runs.

**Sensitive Data:** Real PII and financial data are never used in test
environments. We use tokenization or synthetic replacement. Compliance
reviews confirm that test data policies are followed.
"""  # noqa: E501

version = "0.0.1"
