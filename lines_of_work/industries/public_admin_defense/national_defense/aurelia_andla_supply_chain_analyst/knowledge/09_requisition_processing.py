title = "Requisition Processing (MILSTRIP)"

content = """
- Standard document numbers in scope: A01A (stock replenishment), A02A (MRO/TBO), A04A (issue), A05A (release), A07 (cancellation), A0B (post-post).
- Each document is keyed by a 14-digit transaction code; the analyst verifies the DoDAAC, fund code, and project code triplet before releasing for action.
- Reject conditions: unverified project code, mismatched UIC, invalid signal code, or an SCC inconsistent with the stock status (e.g., SCC "D" on a serviceable item).
- Use DLA Transaction Services for status pull; do not rely on read-only eCatalog tables for current status, as those lag by 4–8 hours.
- For "due-out" documents (A02A), confirm an open in-work order reference before releasing a follow-up issue; otherwise mark the document as "no supply action."
"""  # noqa: E501

version = "0.0.1"
