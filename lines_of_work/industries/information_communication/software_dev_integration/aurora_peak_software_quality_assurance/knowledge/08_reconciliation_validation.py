title = "Reconciliation and Balance Validation Testing"

content = """
Financial systems must maintain balance integrity: debits equal credits,
ledgers reconcile, and aggregations match source data. Testing reconciliation
logic is critical at Aurora Peak.

**What We Test:** We verify that transaction postings produce correct
balances, that inter-system reconciliations succeed, and that reporting
aggregates match underlying records. We test both happy paths and
exception scenarios (partial failures, retries, reversals).

**Test Data Design:** Reconciliation tests require coherent datasets:
transactions, expected balances, and timestamps that align. We use
synthetic data generators and known-good snapshots to build reliable
test environments.

**Automation:** Reconciliation checks are highly automatable. We run
balance validations as part of nightly regression. Any mismatch
triggers an alert and blocks release until resolved.
"""  # noqa: E501

version = "0.0.1"
