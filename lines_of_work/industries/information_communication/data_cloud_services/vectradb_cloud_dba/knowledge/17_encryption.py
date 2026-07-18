title = "Encryption Standards"

content = """
- At rest: AES-256 via the cloud provider KMS (AWS KMS, GCP KMS, Azure Key Vault). Volumes created with Encrypted=true; backups are SSE-S3 with a customer-managed key (CMK).
- In transit: TLS 1.2 minimum, TLS 1.3 preferred. PostgreSQL ssl_min_protocol_version TLSv1.2, ssl_ciphers restricted to AEAD suites. MySQL tls_version TLSv1.2.
- Key rotation: CMK annual rotation via KMS; secrets in HashiCorp Vault rotated every 90 days.
- Tenant BYOK supported on Enterprise plan: tenant uploads key reference, VectraDB never sees the plaintext.
- Encryption verified quarterly: decrypt a sample backup to a sandbox cluster and confirm plaintext is not retrievable from the storage volume after deletion.
"""  # noqa: E501

version = "0.0.1"
