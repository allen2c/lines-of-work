title = "Downtime Tracking: Codes, Recording, and Analysis"

content = """
Downtime tracking is the systematic recording of every period in which a machine or work cell is not producing parts. Accurate downtime data is the foundation of OEE calculation, maintenance prioritization, and continuous improvement. Without it, problems are invisible and recurring failures go unaddressed.

**Downtime categories at Ridgecrest.** All downtime is classified using a standardized code set:

- **Planned downtime (does not reduce OEE planned time):**
  - PM: Scheduled preventive maintenance
  - BRK: Scheduled operator breaks and meals
  - CLN: Planned cleaning and 5S activities
  - TRN: Operator training on the machine

- **Unplanned downtime (reduces OEE availability):**
  - MBD: Machine breakdown (mechanical failure)
  - ELD: Electrical/controls failure
  - TLD: Tooling failure or replacement
  - MAT: Material shortage—no material at machine
  - QHD: Quality hold—waiting for QA disposition
  - OPW: Operator absence or wait
  - PGM: CNC program error requiring correction
  - UTL: Utility failure (air, coolant, power)
  - OTH: Other (requires written description)

**Recording requirements.** The operator records downtime in real time, not at end of shift. For each downtime event, the operator logs: machine ID, start time, end time, downtime code, and a brief description (one sentence). This is entered at the production terminal or on the shift log. Events longer than 10 minutes require the maintenance or supervisor notification regardless of code.

**Escalation.** Any unplanned downtime event exceeding 30 minutes triggers an automatic escalation notification to maintenance and the production supervisor via the production monitoring system. Events exceeding 2 hours require a written maintenance work order with root cause documented.

**Analysis.** The maintenance team reviews a weekly downtime Pareto report—ranked by total hours lost per machine. The top three recurring failure modes by machine receive formal corrective action. PM intervals are adjusted based on actual failure patterns rather than manufacturer defaults alone.

Operators who accurately report downtime, including when a machine runs slowly or intermittently, contribute directly to faster problem resolution. Underreporting to avoid scrutiny delays corrective action and increases total downtime over time.
"""

version = "0.0.1"
