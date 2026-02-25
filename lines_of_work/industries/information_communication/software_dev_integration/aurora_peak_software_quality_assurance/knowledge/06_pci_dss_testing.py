title = "PCI-DSS Testing Requirements for Payment Systems"

content = """
Payment Card Industry Data Security Standard (PCI-DSS) requires specific
controls around cardholder data. Testing must demonstrate that we meet
these requirements and that controls remain effective over time.

**Scope of PCI Testing:** We test access controls, encryption of data
at rest and in transit, vulnerability management, and logging. Each
requirement maps to test cases that validate implementation. Penetration
testing and vulnerability scans are conducted periodically by qualified
assessors.

**Data Handling:** Tests verify that card numbers are never stored in
plaintext, that logs do not contain sensitive data, and that access
is restricted to authorized personnel and systems. Test data must never
include real card numbers.

**Audit Evidence:** Test results, scan reports, and remediation records
form part of our PCI compliance evidence. We maintain traceability from
requirement to test to result for assessor review.
"""  # noqa: E501

version = "0.0.1"
