title = "Batch Processing Schedules"

content = """
Batch processing runs on defined schedules. Merchants should understand
cut-off times to plan settlement expectations.

**Card Batching:** Transactions are batched and submitted to the scheme
according to configured batch close times. Multiple batches per day may
be available. Transactions captured after a batch close settle in the
next batch. Batch times are documented in the partner portal.

**SEPA Batching:** SCT and SCT Inst have cut-off times. SCT Inst executes
in real time; no batching. Standard SCT submitted before cut-off typically
settles T+1.

**Holiday and Weekend Handling:** Banking holidays and weekends affect
settlement. SEPA follows TARGET2 calendar. Card schemes have their own
holiday calendars. Plan for delayed settlement around holidays.

**Batch Reports:** After each batch, merchants can retrieve batch reports
via API or dashboard. Reports list transaction IDs, amounts, and status.

**Configuration Changes:** Batch schedule or cut-off time changes require
advance notice. Contact Technical Integration or your account manager for
modifications.
"""  # noqa: E501

version = "0.0.1"
