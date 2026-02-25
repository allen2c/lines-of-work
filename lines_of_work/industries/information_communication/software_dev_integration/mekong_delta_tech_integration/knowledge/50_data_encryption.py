title = "Mã hóa dữ liệu"

content = """
Encryption bảo vệ data at rest và in transit. Integration phải ensure encryption
cho sensitive data. Mekong Delta Tech encrypt PII và financial data.

**In Transit:** TLS cho mọi connection. No plain HTTP cho sensitive. Certificate
validation. No self-signed trong production (trừ internal với proper CA).

**At Rest:** Encrypt database, backup. Transparent encryption (DB feature) hoặc
application-level. Key management. Encrypt before store. Decrypt on read. Field-level
encryption cho PII.

**Key Management:** Separate from data. HSM hoặc KMS. Key rotation. Don't store
key với data. Access control cho key. Audit key usage.

**Integration:** Encrypt payload khi gửi qua third-party. Agree on algorithm.
Key exchange secure. Consider envelope encryption — encrypt DEK với KEK, store
encrypted DEK với data.
"""  # noqa: E501

version = "0.0.1"
