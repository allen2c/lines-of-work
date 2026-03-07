"""B2B communication protocols for Indus Gateway."""

title = "B2B Communication"

content = """
Indus Gateway communicates with customers and carriers via structured channels.
ASN (Advance Shipping Notice), order confirmations, and status updates follow
agreed formats — EDI, API, or templated email where electronic integration
is not available.

**ASN:** Inbound shipments should be preceded by ASN. Warehouse uses ASN to
prepare receiving, validate expected vs actual, and flag discrepancies early.

**Order Confirmations:** Outbound orders confirmed with expected ship date,
carrier, and tracking reference. Changes or delays communicated promptly.

**Escalation:** Critical issues (customs hold, damage, shortage) require
immediate phone or WhatsApp contact to designated customer representative.
"""  # noqa: E501

version = "0.0.1"
