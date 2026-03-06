title = "Testing Data Pipelines"

content = """
Pipeline tests include unit tests (transform logic with fixture data), integration
tests (end-to-end with test sources), and data quality tests (expectations on
output). dbt supports built-in tests (unique, not_null, relationships) and
custom assertions. Use small, deterministic datasets for unit tests. Integration
tests run in isolated environments. Data quality checks run in production as
monitors. Rhein Cloud requires tests for all new pipelines; coverage targets
apply to critical paths. Tests must be fast and repeatable; avoid flaky
external dependencies.
"""

version = "0.0.1"
