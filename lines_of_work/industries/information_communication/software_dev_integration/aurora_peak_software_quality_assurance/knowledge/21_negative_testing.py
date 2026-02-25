title = "Negative Testing and Error Path Validation"

content = """
Negative testing validates that the system behaves correctly when
given invalid inputs, unexpected conditions, or malicious attempts.
Financial systems must reject invalid operations gracefully.

**Invalid Input:** We test with malformed data, wrong types, out-of-range
values, and boundary violations. The system must reject invalid input
with clear error messages and without corruption or crash.

**Exception Handling:** We simulate failures: database unavailable,
network timeout, external service down. The system should handle
these without data loss, and with appropriate user feedback and
logging. Recovery procedures should be testable.

**Security Negative Tests:** We test authentication failures, expired
sessions, and authorization bypass attempts. The system must deny
unauthorized access and log attempts.
"""  # noqa: E501

version = "0.0.1"
