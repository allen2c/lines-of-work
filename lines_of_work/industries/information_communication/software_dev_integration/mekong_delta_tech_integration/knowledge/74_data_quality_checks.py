title = "Data Quality Checks"

content = """
Data quality check validate data qua integration pipeline. Catch issue early.
Mekong Delta Tech có data quality checks trong ETL và integration.

**Types:** Completeness (no null khi required). Validity (format, range).
Uniqueness (no duplicate). Consistency (cross-field, cross-source). Timeliness
(fresh). Accuracy (against source). Define rules per field, per integration.

**Implementation:** Check in pipeline. Fail or quarantine. Metric per rule.
Dashboard. Alert when quality drop. Threshold. Trend. Root cause when fail.

**Handling:** Reject invalid record. Log. DLQ. Fix upstream. Manual review.
Don't silently drop. Report. SLA cho data quality. Improvement loop.

**Integration:** Contract với partner về data quality. Validate incoming.
Monitor outgoing. Escalate quality issue. Define acceptable threshold.
"""  # noqa: E501

version = "0.0.1"
