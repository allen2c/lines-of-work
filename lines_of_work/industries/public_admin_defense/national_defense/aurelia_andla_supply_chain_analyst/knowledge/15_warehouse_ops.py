title = "Warehouse Operations Touchpoints"

content = """
- Storage activities report on-hand via D043 SAW. The analyst reads the daily warehouse snapshot at 0600 and notes any "hold" lines (SCC "H" or "J").
- Pick/put-away logic is owned by the storage activity; the analyst provides the demand-driven position recommendations, not the slotting plan.
- Net-Position report: reconcile in-place + due-in - due-out against ASR weekly; variance > ±2% is a flagged item.
- Returns (RCS, A04A with return-purpose code) are processed in coordination with Retrograde; the analyst only flags quantity mismatches.
- For each storage activity, the analyst maintains a "missed receipt" list and works with the Receiving Cell to clear items > 10 days outstanding.
"""  # noqa: E501

version = "0.0.1"
