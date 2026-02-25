title = "Work Order Creation, Release, and Closure"

content = """
A work order (also called a production order or shop order) is the formal authorization to manufacture a specific quantity of a specific part or assembly. At Ridgecrest Metalworks, every production activity is linked to a work order. This linkage enables cost tracking, material consumption recording, labor reporting, and traceability.

**Work order creation.** Work orders are created in SAP by the production planner, either automatically from MRP or manually for special jobs. Each work order contains:
- Work order number (unique)
- Material (part) number and description
- Order quantity
- Required completion date
- Routing (list of operations with work centers and standard times)
- Bill of materials (components and quantities to be consumed)
- Customer sales order reference (for make-to-order parts)

**Pre-release checks.** Before a work order is formally released to the shop floor, the planner verifies:
- All required raw materials are in stock or have confirmed delivery dates before the first operation's scheduled start.
- Engineering drawings and specifications are at their current approved revision.
- Any special tooling, fixtures, or programs required are available.
- The work center has available capacity in the planned time window.

**Release.** Releasing the work order generates the shop traveler document and makes the order visible on the cell supervisor's scheduling board. The warehouse team can now pick and issue components.

**Execution.** At each routing step, the operator records: operation start time, quantity produced, quantity scrapped (with scrap code), and operation end time. This is recorded by scanning at the production terminal or on the paper traveler. Time and quantity data feed the production confirmation in SAP.

**Closure.** After the last operation is confirmed and QA final inspection is complete, the warehouse team posts goods receipt from production to move finished parts to inventory. The planner then technically closes the work order in SAP. A closed order calculates the final production variance (actual cost vs. standard cost) for the finance team.

Work orders must be closed within 5 business days of physical completion. Open orders that linger consume system capacity and distort WIP inventory values.
"""

version = "0.0.1"
