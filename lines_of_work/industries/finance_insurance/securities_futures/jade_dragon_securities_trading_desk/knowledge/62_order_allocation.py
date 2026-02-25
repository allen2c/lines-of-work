title = "Order Allocation"

content = """
Order allocation distributes fills from aggregated or block orders
to underlying client accounts. Fair and documented allocation
is essential for compliance and client trust.

**Pro-Rata** allocation distributes fills proportionally to
order sizes. Simple and transparent when orders are simultaneous.

**Time Priority** may apply when orders arrive at different times.
Earliest order receives first fill when price and size match.

**Custom Allocation** may be agreed with clients. Document
agreements and apply consistently.

**Partial Fills** require allocation across participants.
Allocation methodology must be predetermined and documented.
"""

version = "0.0.1"
