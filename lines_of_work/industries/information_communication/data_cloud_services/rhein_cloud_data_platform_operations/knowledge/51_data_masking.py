title = "Data Masking"

content = """
Data masking replaces sensitive values with anonymized or pseudonymized
equivalents for non-production environments. Rhein Cloud applies masking for
development, testing, and analytics access where full PII is not required.

**Static vs Dynamic:** Static masking creates permanent copies with masked
values; dynamic masking applies at query time. Use static for test datasets,
dynamic for shared analytics environments where role-based unmasking is needed.

**Techniques:** Substitution (replace with realistic fake data), shuffling
(permute within column), redaction (partial hide), and hashing. Choose based
on use case and reversibility requirements.
"""

version = "0.0.1"
