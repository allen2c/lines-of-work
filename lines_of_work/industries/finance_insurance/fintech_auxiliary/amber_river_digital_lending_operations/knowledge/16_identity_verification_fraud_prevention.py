title = "Identity Verification and Fraud Prevention for Digital Lending"

content = """
Digital lending relies on remote identity verification. Amber River
uses a layered approach to confirm applicant identity and detect
fraud before disbursement.

**Document Verification:** Applicants upload a government-issued ID
(driver's license, passport). We verify document authenticity,
expiration, and match to the applicant's stated information.
Liveness checks may be required to prevent use of stolen or
altered documents.

**Database and Knowledge-Based Verification:** We cross-reference
applicant data against trusted sources (e.g., credit bureau,
utility, or public records) to confirm identity and address.
Knowledge-based authentication (KBA) questions may be used for
additional assurance.

**Synthetic Identity and First-Party Fraud:** We screen for
synthetic identities (fabricated identities combining real and
fake data) and first-party fraud (applicants who intend to
default). Behavioral signals, device fingerprinting, and
velocity checks support detection.

**Red Flags:** Multiple applications in short period, mismatched
address or contact information, suspicious document quality,
or inconsistent income claims may trigger manual review or
denial. We do not disclose specific fraud indicators to
applicants.

**Escalation:** Suspected identity theft or fraud is escalated
to the Fraud and Identity team. Operations does not approve
or deny applications; we guide applicants through the process
and route concerns appropriately.
"""  # noqa: E501

version = "0.0.1"
