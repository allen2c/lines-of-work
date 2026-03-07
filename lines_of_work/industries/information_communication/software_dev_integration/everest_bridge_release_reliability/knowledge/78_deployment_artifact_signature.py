"""Deployment artifact signing for integrity and provenance."""

title = "Deployment Artifact Signature"

content = """
Artifact signing ensures that deployed binaries and images are authentic and have not
been tampered with. It supports auditability and supply chain security.

**Signing Process:** Sign artifacts (containers, binaries) at build time with a trusted
key. Store signatures in a registry or manifest. Verify signatures before deployment.

**Key Management:** Protect signing keys in a secure store (e.g. HSM, vault). Rotate keys
periodically and document key lifecycle. Limit who can trigger signing.

**Verification:** Deployment pipelines should verify artifact signatures before pulling
or executing. Reject unsigned or invalidly signed artifacts. Log verification results.
"""

version = "0.0.1"
