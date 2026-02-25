title = "API Testing Standards at Aurora Peak"

content = """
Our APIs are the backbone of integrations and internal services. API testing
validates contracts, authentication, error handling, and data correctness.
We use tools like Postman, pytest-requests, and OpenAPI validators.

**Contract Testing:** We verify that API responses match the schema. This
catches breaking changes early. Contract tests run in CI and block merges
if schemas diverge unexpectedly.

**Authentication and Authorization:** APIs must reject unauthorized requests
and enforce role-based access. We test valid tokens, expired tokens,
invalid tokens, and missing tokens. We verify that users cannot access
resources outside their scope.

**Error Handling:** APIs must return appropriate status codes and error
payloads. We test 4xx and 5xx scenarios, validation failures, and
rate limiting. Error messages must not leak sensitive data.
"""  # noqa: E501

version = "0.0.1"
