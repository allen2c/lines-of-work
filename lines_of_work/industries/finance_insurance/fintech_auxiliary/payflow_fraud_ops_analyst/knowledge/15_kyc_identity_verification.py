title = "KYC and Identity Verification"

content = """
- KYC process: collect name, DOB, SSN, address, and government ID. Verify via third-party services (e.g., Jumio, Onfido).
- Liveness check: customer must take a selfie with ID; system compares facial features.
- Failure: if ID is expired, tampered, or does not match selfie, reject application and flag for manual review.
- Enhanced due diligence for high-risk customers (e.g., PEPs, high transaction volume) requires additional documentation.
"""  # noqa: E501

version = "0.0.1"
