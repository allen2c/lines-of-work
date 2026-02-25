title = "Maintenance Work Orders: Raising and Closing Out"

content = """
Maintenance work orders (MWOs) are the formal mechanism for planning, authorizing, executing, and recording all maintenance activities at Ridgecrest Metalworks. The computerized maintenance management system (CMMS) manages all MWOs and provides the historical record of work performed on each asset.

Work orders are generated from three sources:
- Preventive maintenance: The CMMS automatically generates PM work orders based on the scheduled interval for each asset
- Predictive maintenance alerts: Condition monitoring data (vibration, thermography, oil analysis) that triggers a work order when alarm thresholds are exceeded
- Reactive / breakdown: Raised by production or maintenance personnel when equipment fails or a defect is observed

Raising a reactive or corrective MWO: Any employee who identifies a maintenance need can raise a request. The request is entered in the CMMS (or on a paper request where electronic access is not available) with:
- Asset ID and location
- Description of the fault or observed condition (specific and factual: "Bearing noise from motor drive end"; not vague: "Machine not working well")
- Priority: Emergency (production-stopping or safety risk), Urgent (risk of imminent failure), Routine (plannable)
- Date and time raised, and raised-by name

MWO planning: A maintenance supervisor reviews the work order, assigns a technician, identifies required spare parts, and schedules the work. If LOTO is required, the permit-to-work is raised simultaneously. For major overhauls, a job plan listing tasks, tools, parts, and estimated time is attached.

MWO execution: The technician completes the assigned tasks and records on the work order:
- Tasks performed (specific, not just "completed PM")
- Parts replaced (part number, quantity, and where obtained from)
- Measurements taken (bearing temperature, vibration reading, oil level)
- Any additional findings and whether they were corrected or require a follow-up work order
- Labor time
- Date and time completed

Closing an MWO: The technician signs and closes the work order in the CMMS after all work is complete and the equipment has been tested and returned to service. Incomplete or open-ended work orders are reviewed weekly; unclosed work orders from more than 30 days prior are escalated.

CMMS data from MWOs drives maintenance KPIs: planned maintenance compliance, mean time between failures (MTBF), mean time to repair (MTTR), and maintenance cost per asset. This data informs maintenance strategy decisions and spare parts stocking.
"""

version = "0.0.1"
