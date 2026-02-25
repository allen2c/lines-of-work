title = "Engineering Change Orders (ECOs): Floor Impact and Implementation"

content = """
An Engineering Change Order (ECO) is the formal document that authorizes a change to a product design, material specification, manufacturing process, or quality requirement. At Ridgecrest Metalworks, no change to how a part is made may occur without an approved ECO. Unauthorized process changes—even well-intentioned ones—constitute nonconformances under ISO 9001 and can result in customer escapes.

**Why ECOs matter on the floor.** Changes to drawings, tolerances, material grades, weld procedures, surface treatments, or inspection criteria directly affect how operators run their machines and verify their work. An operator working from a superseded drawing is not wrong to do so—the system failed to communicate the change. ECO management closes this gap.

**ECO process.** Engineering generates a change proposal describing the problem, the proposed change, and the affected documents. The change review board (CRB)—including engineering, quality, manufacturing, and supply chain—approves or rejects the change. Upon approval, the ECO is assigned an effective date (can be immediate, tied to a lot date, or tied to a serial number).

**Effectivity types and floor impact:**
- **Immediate effectivity:** All current WIP must be evaluated. Parts already in process may need to be reworked or scrapped depending on the nature of the change. The planner and supervisor assess each open work order against the ECO requirements.
- **Lot date effectivity:** New ECO applies to all work orders released after the effective date. WIP before that date continues under the old specification.
- **Serial/lot number effectivity:** Applies to specific production lots, used when traceability to individual units is required.

**Floor implementation steps.**
1. Receive the ECO notification (posted on the production board and distributed via ERP message).
2. Update drawings and documents at the work cell—remove and destroy superseded revision copies.
3. Review the traveler to confirm the new revision is referenced.
4. Communicate the change to all operators who run the affected part—document this communication with signatures on the ECO acknowledgment form.
5. If a new first article or first-piece inspection is required by the ECO, complete it before running production quantities.

**Parts already completed.** If finished parts in inventory are affected by the ECO, quality must disposition them. Options: rework to new specification, use-as-is with customer concession, or scrap.

ECOs are never "informational only" on the floor—they always require a defined action.
"""

version = "0.0.1"
