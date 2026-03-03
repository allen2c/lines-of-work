title = "Reconciliation Processes"

content = """
Reconciliation ensures merchant records match Nordstern settlement statements.
Discrepancies must be identified and resolved promptly.

**Statement Components:** Settlement statements include: gross transaction
amounts, fees, refunds, chargebacks, adjustments, and net payout amount.
Each line item references transaction or batch IDs for matching.

**Reconciliation Frequency:** Merchants should reconcile daily for high-volume
accounts, at least weekly for others. Delayed reconciliation extends the
window for unreported discrepancies.

**Common Discrepancies:** Timing differences (transactions in different
settlement batches), fee calculation questions, chargebacks not yet
reflected in merchant system, or duplicate posting. Most resolve with
batch and transaction ID cross-reference.

**Dispute Window:** Merchant agreements specify how long after settlement
merchants can dispute statement line items. Beyond that window, disputes
may not be considered.

**Reporting:** Nordstern provides downloadable CSVs and access to reporting
APIs for automated reconciliation. Merchants with custom ERP or accounting
systems can integrate via API.
"""  # noqa: E501

version = "0.0.1"
