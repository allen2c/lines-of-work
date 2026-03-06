title = "Data Aggregation for Regulatory Reporting"

content = """
Regulatory reports often require data from multiple internal systems: trading, risk,
accounting, and client onboarding. Aggregation must be accurate, consistent, and
traceable.

**Data sources:** Trade capture, position management, NAV calculation, counterparty
master data, and collateral systems. Data may reside in different formats and
update frequencies. Reconciliation between sources is critical.

**Golden source:** Establishing a single source of truth for each data element
reduces errors. Data governance defines ownership, quality rules, and lineage.
Transformations and mappings should be documented and tested.

**Timing:** Reporting deadlines are strict. Data must be available, validated,
and transformed in time. Batch schedules and dependencies must be managed.
Late or incorrect data can trigger regulatory scrutiny.
"""  # noqa: E501

version = "0.0.1"
