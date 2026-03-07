"""Shipment tracking and visibility for Indus Gateway."""

title = "Shipment Tracking"

content = """
Indus Gateway tracks shipments from warehouse dispatch to final delivery. Tracking
numbers are assigned at outbound and shared with customers via B2B portal or email.

**Carrier Integration:** Major carriers (TCS, Leopards, BlueEx, international
forwarders) provide tracking APIs. WMS links order ID to carrier tracking number.

**Status Updates:** Pro forma statuses: picked, packed, dispatched, in transit,
customs hold, delivered. Customers receive automated notifications at key milestones.

**Exception Handling:** Delays, customs holds, or failed delivery attempts trigger
alerts. Operations team contacts carrier and customer to resolve. All exceptions
logged for root-cause analysis.
"""  # noqa: E501

version = "0.0.1"
