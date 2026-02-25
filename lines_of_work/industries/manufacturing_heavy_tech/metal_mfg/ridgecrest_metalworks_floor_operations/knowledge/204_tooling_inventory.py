title = "Production Tooling Inventory and Life Tracking"

content = """
Production tooling — cutting tools, forming dies, press tooling, jigs, fixtures, and gauges — represents a significant capital investment at Ridgecrest Metalworks. Effective tooling inventory management ensures that production tooling is available when needed, maintained in serviceable condition, and replaced before failure causes quality or safety problems.

Tooling classification and tracking:

Perishable tooling: Single-use or limited-life cutting tools (drills, end mills, taps, inserts, saw blades, grinding wheels). These are consumed in production and replenished from the tool store. Tool life data — measured in parts produced, running time, or linear meters cut — is tracked per tool type and operation. When tool life limits are reached, the tool is changed regardless of apparent condition.

Regrindable tooling: Solid carbide drills, end mills, and form cutters that can be resharpened multiple times. These are tracked by individual tool ID. Each regrind is recorded; a maximum number of regrind cycles is set (beyond which the tool geometry is outside useful tolerance) and the tool is replaced at this limit.

Toolholders and adapters: Hydraulic, shrink-fit, ER collet, and Capto toolholders are durable items that must be inspected for runout at defined intervals. Toolholder runout above 5 µm (measured at the cutting edge plane) causes premature tool wear and poor surface finish. Damaged or out-of-tolerance toolholders are removed from the CNC and sent for reconditioning or replaced.

Hard tooling (dies, molds, jigs, fixtures): These are registered assets with individual IDs, stored in the tool room on labeled racks. Each tool has a maintenance record documenting:
- Material and design specification (drawing reference)
- In-service date and total parts produced (struck count)
- Maintenance history (surface regrinding, insert replacement, dimension restoration)
- Condition assessment at last use

Tool life management: For high-volume press tooling and forming dies, a preventive maintenance interval is set (e.g., every 10,000 hits for piercing dies; every 5,000 hits for progressive dies). At this interval, the die is removed, inspected, punch and die clearances measured, and worn inserts replaced before failure occurs. Failure of a die in service (punch breakage, die cracking) causes production disruption and may damage the press.

Tooling kitting: When a production job is released, the tooling kitter pulls all required tools from the store and assembles them into a kit for the machine operator. Tool kitting eliminates mid-run searches for tooling and ensures the correct tools are available at the machine before setup begins.
"""

version = "0.0.1"
