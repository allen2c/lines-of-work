title = "Integration Testing for Data Pipelines"

content = """
Integration tests verify that pipeline components work together correctly across
source systems, staging, transformation, and target. Rhein Cloud runs integration
tests in a dedicated test environment before production promotion. Tests cover
end-to-end flows, schema compatibility, and data volume handling. Failures block
deployment until resolved. Test data is anonymized and refreshed periodically.
"""

version = "0.0.1"
