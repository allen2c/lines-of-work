title = "SOAP Security"

content = """
SOAP/WS-Security phức tạp. Signature, encryption, token. Legacy integration
cần handle. Mekong Delta Tech support SOAP security khi integrate legacy.

**WS-Security Header:** Signature, Encryption, Security token. XML structure.
Library handle (python Zeep, etc). Certificate. Key store. Configure correctly.
Test với real partner.

**Authentication:** Username token. Certificate. SAML. Kerberos. Depends on
partner. Document. Configure. Credential management. Rotate. Secure storage.

**Encryption:** Encrypt body, header. Algorithm. Key exchange. Performance.
Decrypt at adapter. Re-encrypt nếu forward. Compliance. Document.

**Signature:** Verify signature. Sign response. Non-repudiation. Timestamp.
Replay attack prevention. Validate. Library support. Test.
"""  # noqa: E501

version = "0.0.1"
