title = "CMMS and Equipment Asset Management"

content = """
A Computerized Maintenance Management System (CMMS) is the software backbone of
maintenance operations at Ridgecrest Metalworks. It stores equipment records,
schedules preventive maintenance tasks, tracks work orders from creation to
closure, and accumulates historical failure data for reliability analysis.
Operators and maintenance technicians interact with the CMMS daily.

**Core CMMS Functions:**

- **Equipment Registry:** Every production asset has a unique equipment ID, linked
  to its technical specifications, spare parts list, maintenance history, and
  associated documents (manuals, drawings, certifications).

- **Work Order Management:** Corrective, preventive, and predictive work orders
  are raised, assigned, and closed in the CMMS. Each work order records labor
  hours, parts consumed, failure mode, and completion notes.

- **Preventive Maintenance (PM) Scheduling:** PM tasks trigger automatically based
  on calendar intervals (weekly, monthly, quarterly, annually) or meter readings
  (running hours, cycle counts). The planner reviews the upcoming PM backlog each
  week.

- **Spare Parts Inventory:** The CMMS links to the stores inventory, tracking
  part consumption per work order and generating reorder alerts when stock drops
  below the minimum level.

- **Failure Reporting:** Technicians select a failure mode from a standardized
  taxonomy (e.g., bearing failure, seal leak, electrical fault) when closing
  corrective work orders. This data feeds reliability-centered analysis.

**Raising a Corrective Work Order (Operator Procedure):**
1. Observe and describe the fault clearly (location, symptom, time of onset).
2. Log into the CMMS terminal or use the floor tablet to raise a notification.
3. Select the equipment ID and fault description from dropdown menus.
4. Assign urgency: Emergency (immediate production stoppage), Urgent (degraded
   performance), or Routine (no immediate production impact).
5. Notify the maintenance supervisor verbally for Emergency or Urgent faults.

**Asset Criticality Classification:**
Equipment is classified A (critical — no backup, direct production impact),
B (important — limited backup or workaround available), or C (non-critical —
redundant or easily substituted). Class A assets receive priority PM scheduling
and mandatory spare parts stocking. Operators must immediately report any Class A
anomaly, regardless of apparent severity.

**Key Performance Metrics from CMMS:**
- Planned Maintenance Compliance (PMC): % of PM tasks completed on schedule.
- Mean Time Between Failures (MTBF): Average operating time between corrective
  work orders for a given asset.
- Mean Time to Repair (MTTR): Average time from fault detection to return to
  service.
- Backlog hours: Total outstanding maintenance labor, used to plan staffing.
"""

version = "0.0.1"
