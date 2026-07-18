title = "Chargeback Lifecycle Overview"

content = """
- The chargeback lifecycle consists of five stages: Transaction, Dispute, Chargeback, Representment, and Pre-Arbitration/Arbitration.
- Stage 1: A cardholder initiates a dispute with their issuing bank. The issuer sends a chargeback to the acquirer (NexPay) with a reason code.
- Stage 2: NexPay receives the chargeback notification via the card network. The analyst must log it within 2 hours.
- Stage 3: The merchant can accept the chargeback or provide representment evidence. If no response within the SLA, the chargeback is automatically lost.
- Stage 4: Representment is submitted to the network. The issuer reviews and either accepts (reversal) or rejects (second chargeback).
- Stage 5: If the issuer rejects, the merchant may request pre-arbitration (Visa) or arbitration (Mastercard). This is a final review by the network.
"""  # noqa: E501

version = "0.0.1"
