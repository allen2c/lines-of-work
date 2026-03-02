title = "SEPA Instant Payments"

content = """
SEPA Instant Credit Transfer (SCT Inst) enables real-time euro transfers across
participating banks in the Single Euro Payments Area. Nordstern offers SCT Inst
for payouts and wallet credits where speed is critical.

**Execution Time:** Transactions complete within seconds, 24/7/365, including
weekends and holidays. Unlike standard SCT, there is no batch delay.

**Transaction Limit:** Maximum €100,000 per transaction. Higher amounts require
standard SCT or multiple instant transfers.

**Reach:** Not all SEPA banks support SCT Inst. Before processing, verify
beneficiary bank participation via the EPC SCT Inst scheme register. Failed
instant attempts may fall back to standard SCT if configured.

**Fees:** SCT Inst carries a premium over standard SCT due to real-time
processing and liquidity requirements. Pricing is per-transaction.

**Use Cases:** Instant payouts to gig workers, urgent refunds, real-time
wallet top-ups, time-sensitive B2B payments. Avoid for high-volume batch
payouts where standard SCT cost savings matter more than speed.

**Reversal:** SCT Inst supports request for recall within defined time windows
if sent in error. Outcomes depend on beneficiary bank response.

**Status and Error Handling:** Instant payments return immediate success or
failure. Common failure reasons: beneficiary bank not reachable, daily limit
exceeded, invalid account details.
"""  # noqa: E501

version = "0.0.1"
