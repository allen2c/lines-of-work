title = "Cycle Counting Procedures and Reconciliation"

content = """
Cycle counting is a perpetual inventory audit method in which a portion of the total inventory is counted on a rotating basis, so that every item is physically verified at least once per year without requiring a full facility shutdown. At Ridgecrest Metalworks, cycle counting is the primary mechanism for maintaining inventory accuracy and catching discrepancies before they affect production or financial reporting.

**Count frequency.** Items are classified into A, B, and C categories based on annual value consumption:
- A items (top 20% by value): counted monthly.
- B items (next 30%): counted quarterly.
- C items (remaining 50%): counted twice per year.

**Who performs counts.** Counts are performed by trained inventory personnel, not by the operators who routinely handle that material. This independence ensures counts are not influenced by operator knowledge or assumptions about what should be there.

**Count process.**
1. The inventory controller prints count sheets that list material number, description, and storage location—but intentionally omit the ERP on-hand quantity to prevent anchoring bias.
2. Counters go to the physical location, count every item, and record actual quantity on the count sheet. Count by unit of measure (pieces, pounds, feet—not by "about a full rack").
3. Counts are entered into the ERP count document. The system compares to the book quantity and calculates variances.
4. Variances within the tolerance threshold (±2% for A items, ±5% for B and C) are auto-approved and the book is adjusted.
5. Variances above threshold trigger a recount—a second independent counter repeats the physical count before any adjustment is made.

**Reconciliation.** If the recount confirms a variance above threshold, a root-cause investigation is mandatory. Common causes include: missed goods issues, goods receipts posted to wrong locations, material moved without system transaction, or theft. The investigation finding is documented and corrective action is assigned.

**Frozen inventory during count.** No material may be issued, received, or moved from a location actively being counted. Transactions resume only after the count record is confirmed.

Cycle count accuracy is reported to management monthly. Consistent accuracy below 95% triggers a systemic process review.
"""

version = "0.0.1"
