"""Release compliance checks for regulatory and policy requirements."""

title = "Release Compliance Checks"

content = """
Compliance checks ensure releases meet regulatory, security, and internal policy
requirements before deployment. These checks may be mandatory for certain industries
or data types.

**Check Types:** License compliance for dependencies, vulnerability scanning, data
retention and privacy checks, audit logging configuration, and change approval
documentation.

**Automation:** Integrate compliance checks into the pipeline where possible. For
manual checks, define clear criteria and sign-off requirements. Store evidence for
audit purposes.

**Remediation:** Failed compliance checks block release until resolved or formally
waived. Document waivers with justification and expiry. Conduct periodic compliance
reviews.
"""

version = "0.0.1"
