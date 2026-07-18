title = "Structured Log Analysis with NCS"

content = """
- NCS ingestion limit per account is 500 GB/day by default; the soft alert threshold is 80% (400 GB/day). Higher tiers can request an increase.
- Query language is a SQL-like dialect: filter on `field=value`, time range with `@timestamp`, and pipe into aggregations.
- For a "sudden 5xx spike" investigation, the standard query is `filter @type = "REPORT" and statusCode >= 500 | stats count() by statusCode, bin(5m)`.
- PII redaction: NCS supports field-level masking; never store raw tokens, passwords, or PAN data in log groups. The Data Handling Policy mandates scrubbing within 24 hours of detection.
- Cross-region log copying has a 5-10 minute delay; do not promise real-time parity.
"""  # noqa: E501

version = "0.0.1"
