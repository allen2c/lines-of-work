title = "FIFO Stock Rotation in Metal Storage"

content = """
First-In, First-Out (FIFO) is a stock rotation method that ensures the oldest material in inventory is consumed before newer material. In metal manufacturing, FIFO is not just an accounting convention—it is an operational discipline that protects against corrosion, certification expiry, and material specification drift.

**Why FIFO matters for metal.** Steel and aluminum oxidize over time. Even with protective coatings, prolonged storage can lead to surface rust, pitting, and reduced material properties. For heat-treated alloys and stainless grades, extended storage in improper conditions can affect microstructure. Beyond physical degradation, regulatory and customer requirements may specify maximum time limits between mill certification and use in production.

**How FIFO is enforced at Ridgecrest.** Each storage location is managed so that newly received material is placed behind or below existing stock whenever physically feasible. The receipt date appears on every incoming label. When issuing material to a work order, personnel must select the oldest lot first—confirmed by checking the receipt date on the ERP location report or on the physical label.

**Rack and floor stack practices.** Cantilever rack sections for bar stock and tubing are loaded from the rear using a drive-through or push-back approach. Operators issue from the front. For floor-stacked plate bundles, new bundles are placed to the back or side of the stack, and the oldest is issued first. A "use next" tag on the designated oldest bundle provides a clear visual cue.

**Exceptions.** If a newer lot has been released from a quality hold while the older lot is still in quarantine, the older lot must not be used until it receives QA clearance—even though it has the earlier date. In this case, the QA release date takes precedence over the receipt date. Document any FIFO deviation on the work order traveler and notify the supervisor.

**Cycle count verification.** During cycle counts, auditors check date labels against the ERP receipt date. Lots issued out of sequence generate a discrepancy report that production planning reviews to identify whether scheduling or physical practices need correction.

FIFO compliance is audited as part of ISO 9001 internal audits and select customer supplier audits.
"""

version = "0.0.1"
