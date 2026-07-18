title = "Exception Management"

content = """
- A "supply exception" is any condition where the on-hand or due-in position is below the prescribed threshold, the receipt is overdue, or the contract performance deviates beyond tolerance.
- Each exception has: an entry timestamp, a documented owner, an estimated recovery date, and a closure note.
- Tiering: Tier 1 (safety-level breach on a C-rated item), Tier 2 (ROP breach on a D-rated item or its components), Tier 3 (all other breaches). Tier 1 escalates within the same business day.
- The analyst maintains the active exception list and reviews open items at each daily standup; closed items move to the historical log only after a 5-day cooling period.
- For any exception pending > 30 days, the analyst drafts a recommendation memo for the Section Chief; the memo does not contain any procurement award language.
"""  # noqa: E501

version = "0.0.1"
