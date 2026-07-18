title = "Access Control and Audit"

content = """
- Authentication: SCRAM-SHA-256 for PostgreSQL, caching_sha2_password for MySQL, x.509 for MongoDB, password plus TLS for ClickHouse.
- Authorization: all GRANT and REVOKE flows go through the IAM portal, which emits a signed request to the access-broker service that issues a 15-minute single-purpose token. No long-lived DB passwords.
- Roles follow least privilege: app_read, app_write, app_admin (per schema), migrator (DDL only, time-bound), auditor (read-only across all schemas).
- Audit log: pgaudit for PostgreSQL, audit_plugin for MySQL, auditLog for MongoDB, shipped to S3 with 7-year retention; tampering is detected via daily hash chain verification.
"""  # noqa: E501

version = "0.0.1"
