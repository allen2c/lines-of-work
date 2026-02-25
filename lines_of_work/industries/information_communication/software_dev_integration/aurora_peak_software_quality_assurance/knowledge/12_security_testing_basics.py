title = "Security Testing Basics for Fintech"

content = """
Security testing validates that our applications resist common attacks and
protect sensitive data. We combine automated scanning with manual
assessment for critical areas.

**Automated Scanning:** SAST (static analysis) and DAST (dynamic scanning)
run in CI and on schedules. We fix high and critical findings before
release. Medium findings are triaged and scheduled.

**Authentication and Session Testing:** We test for broken authentication,
session fixation, and privilege escalation. Password policies, lockouts,
and multi-factor flows are validated.

**Injection and Input Validation:** SQL injection, XSS, and command injection
are tested via both automated tools and manual probing. We verify that
all inputs are validated and sanitized before use.

**Data Protection:** We confirm that sensitive data is encrypted in transit
(TLS) and at rest. We verify that logs and error messages do not expose
sensitive information. Access controls are tested for bypass attempts.
"""  # noqa: E501

version = "0.0.1"
