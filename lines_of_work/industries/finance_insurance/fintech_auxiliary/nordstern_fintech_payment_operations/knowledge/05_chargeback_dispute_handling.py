title = "Chargeback and Dispute Handling"

content = """
Chargebacks occur when a cardholder disputes a transaction with their bank.
Merchants must respond with evidence within scheme-defined timeframes or lose
the dispute and the funds.

**Chargeback Reasons:** Common codes include: fraudulent transaction (10.x),
product not received, duplicate processing, cancellation or return disputes,
and authorization issues. Each reason code has specific evidence requirements.

**Representment:** Merchants can represent (contest) chargebacks by submitting
compelling evidence: delivery confirmation, signed receipts, terms of service
acknowledgment, or proof of prior refund. Evidence must directly address the
cardholder's claim. Representment deadlines are strict — typically 7–21 days
depending on reason code.

**Prevention:** Reduce chargebacks by: clear product descriptions, reliable
shipping and tracking, responsive customer service, and immediate refunds
for valid returns. 3D Secure adoption shifts liability for fraud chargebacks
to the issuing bank when SCA succeeds.

**SEPA Direct Debit Returns:** Unlike card chargebacks, SEPA direct debit
returns follow mandate and timeline rules. Unauthorized or disputed debits
may be returned within 8 weeks (13 months for unauthorized); mandate
disputes up to 13 months. Merchants must retain mandate evidence.

**Operations Role:** Payment operations provides guidance on documentation
requirements and timelines. Actual representment and dispute handling is
performed by the Fraud and Chargeback team — escalate cases to them.
"""  # noqa: E501

version = "0.0.1"
