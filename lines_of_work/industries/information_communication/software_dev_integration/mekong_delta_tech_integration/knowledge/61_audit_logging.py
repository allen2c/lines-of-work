title = "Audit Logging"

content = """
Audit log ghi mọi thay đổi quan trọng cho compliance và forensic. Integration
cần audit cho sensitive operations. Mekong Delta Tech có audit requirement.

**What to Audit:** CRUD on sensitive data. Auth events (login, permission).
Configuration change. API access. Who, what, when, result. Immutable. Tamper-proof.

**Format:** Structured. Actor, action, resource, timestamp, before/after (when
appropriate), IP, request ID. Store in dedicated audit store. Retention policy.
Searchable. Export for audit.

**Compliance:** PDPA, SOC2, industry-specific. Audit trail required. Retention
period. Access control cho audit data. Report generation.

**Performance:** Async write. Don't block main flow. Batch when high volume.
Dedicated audit service. Consider impact on latency.
"""  # noqa: E501

version = "0.0.1"
