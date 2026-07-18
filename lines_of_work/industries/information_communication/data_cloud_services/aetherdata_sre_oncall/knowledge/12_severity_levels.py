title = "Severity Level Definitions"

content = """
- **SEV1**: Critical – Complete service outage or data loss. Example: all database clusters unreachable, object storage unavailable.
- **SEV2**: High – Significant degradation for paying customers. Example: p99 latency > 5s, 10%+ error rate, single region down.
- **SEV3**: Medium – Minor degradation or non-critical feature broken. Example: one node down, slow query for internal tool.
- **SEV4**: Low – Informational or cosmetic. Example: disk usage > 70%, certificate expiring in 30 days.
- Severity can be upgraded if impact grows. Downgrade only after incident is resolved.
"""  # noqa: E501

version = "0.0.1"
