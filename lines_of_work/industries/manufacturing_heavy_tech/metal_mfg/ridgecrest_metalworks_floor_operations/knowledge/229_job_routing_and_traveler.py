title = "Job Routing Sheets and Shop Traveler Documents"

content = """
A job routing (or process routing) defines the sequence of operations required to manufacture a part from raw material to finished goods. The shop traveler is the physical or electronic document that accompanies the job through the facility and records that each operation was completed correctly. Together, they are the instruction set and audit trail for every work order at Ridgecrest Metalworks.

**Routing structure.** Each routing step specifies:
- Operation number (in sequence: 10, 20, 30, etc.)
- Work center (machine or cell)
- Operation description (e.g., "Laser cut per DXF file Rev D")
- Setup time (standard hours)
- Run time per piece (standard hours)
- Inspection requirement (yes/no, and which inspection steps)
- Any special notes or referenced instructions

Routing step numbers increment by 10 to allow insertion of new steps without renumbering. If a step is added to a released routing (e.g., an additional deburr step), this constitutes an engineering change that requires formal ECO approval.

**Shop traveler document.** The traveler is printed from SAP when the work order is released. It shows:
- Work order number and part number (with revision)
- Customer name and sales order reference
- Order quantity and required ship date
- All routing operations in sequence
- Material heat/lot number(s) issued to the order
- QC sign-off boxes at designated inspection steps

Each operator who completes a step signs, dates, and records the quantity produced and quantity scrapped in the appropriate traveler box. The traveler must travel physically with the parts—it should never be in a different location than the parts it represents.

**Deviation from routing.** If a process step cannot be completed as specified (e.g., a required machine is down), the supervisor must contact the planner and engineering before routing the parts to an alternate operation. Unauthorized routing deviations create quality escapes and traceability gaps. Any approved deviation is noted on the traveler with supervisor signature.

**Traveler retention.** Completed travelers are collected by the production clerk at work order closure and stored in the job file for a minimum of 10 years, or longer if the customer contract requires it. Travelers are the primary evidence in any customer quality dispute or regulatory audit.
"""

version = "0.0.1"
