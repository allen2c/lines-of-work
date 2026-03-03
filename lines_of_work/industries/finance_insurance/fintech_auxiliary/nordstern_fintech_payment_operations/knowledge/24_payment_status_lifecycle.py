title = "Payment Status Lifecycle"

content = """
Payments move through defined statuses from creation to final settlement.
Understanding the lifecycle helps with customer communication and
reconciliation.

**Card Lifecycle:** pending → authorized → capture requested → captured
→ settled. Failed states: authorization_failed, capture_failed,
canceled. Refunds create separate objects with status refunded.

**SEPA Lifecycle:** initiated → processing → completed (or failed).
SCT Inst completes in seconds. Standard SCT completes when the batch
is processed (typically T+1).

**Status Checks:** Query payment status via API or dashboard. Use
webhooks for real-time updates rather than polling.

**Settlement Finality:** Once settled, the payment is complete. Disputes
and chargebacks can still occur after settlement; these create separate
debit entries and require representment if contested.

**Customer Communication:** For delayed or failed payments, provide
clear status to customers. Avoid over-promising; "pending" does not
guarantee success. For SEPA, "processing" typically means execution
within the batch; completion depends on cut-off times.
"""  # noqa: E501

version = "0.0.1"
