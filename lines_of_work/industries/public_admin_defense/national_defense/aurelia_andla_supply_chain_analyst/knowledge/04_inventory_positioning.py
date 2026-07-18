title = "Inventory Positioning Strategy"

content = """
- Compute Days of Supply (DOS) = On-Hand Balance / Average Daily Demand (rolling 90 days). Round to one decimal.
- Band logic: critical ≤ 15, low 16–30, balanced 31–90, excess 91–180, surplus > 180. Reposition only when an item is in the critical or excess band for two consecutive weekly snapshots.
- Consider safety level (SL), reorder point (ROP), and the Economic Order Quantity (EOQ) for class B/C items; do not apply EOQ logic to CMEL or CIL items.
- For consumables, use the 12-month demand history; for reparables, use the last 8 quarters of computed DLR requirements.
- Reject any proposed redistribution where the losing site would drop below its computed ROP after the move.
"""  # noqa: E501

version = "0.0.1"
