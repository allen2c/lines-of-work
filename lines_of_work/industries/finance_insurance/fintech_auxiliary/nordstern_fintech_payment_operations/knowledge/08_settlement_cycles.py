title = "Settlement Cycles"

content = """
Settlement is the process by which funds from processed payments reach the
merchant's bank account. Timing varies by payment type and configuration.

**Card Settlement:** Typically T+1 or T+2. Transactions authorized and
captured today settle in the next (or next-next) banking day. Batch cut-off
times affect which transactions are included in a given settlement. Weekend
and holiday processing may shift timelines.

**SEPA Credit Transfer:** SCT pays out in one business day (T+1) after
execution. Cut-off times apply; payments initiated after cut-off roll to
the next day.

**SEPA Instant:** Funds arrive in seconds. No batch delay. Availability
in the merchant's account depends on their bank's processing.

**Batching:** Card transactions are batched for scheme submission. Merchants
can often configure batch close times to optimize cash flow. Multiple batches
per day may be available for high-volume merchants.

**Statement Reconciliation:** Settlement statements list transactions,
fees, refunds, and chargebacks. Merchants should reconcile against their
own records. Discrepancies should be reported within the dispute window
specified in the merchant agreement.
"""  # noqa: E501

version = "0.0.1"
