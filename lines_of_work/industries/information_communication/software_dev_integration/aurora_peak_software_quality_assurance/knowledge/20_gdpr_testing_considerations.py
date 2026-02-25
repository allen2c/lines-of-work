title = "GDPR Testing Considerations"

content = """
Applications handling EU personal data must comply with GDPR. Testing
validates that we meet data protection requirements: consent, access
rights, erasure, portability, and breach notification readiness.

**Consent and Legitimate Basis:** We verify that consent is collected
and recorded correctly. We test that features requiring consent
are blocked when consent is withdrawn. Legitimate interest and
other bases are documented and testable.

**Subject Rights:** We test responses to access requests (data export),
erasure requests (right to be forgotten), and portability. Response
times and correctness are validated. We ensure that erasure cascades
to all relevant systems.

**Data Minimization and Retention:** We verify that we collect only
necessary data and retain it only as long as required. Tests confirm
that automated retention and deletion policies function correctly.
"""  # noqa: E501

version = "0.0.1"
