title = "SCADA and EMS Architecture for Grid Operations"

content = """
The Supervisory Control and Data Acquisition (SCADA) system collects real-time data from
plant equipment. The Energy Management System (EMS) uses this data to execute dispatch,
compliance, and optimization functions. Together they form the operational backbone.

**Data Flow:** Inverters, meters, weather stations, and switchgear report to SCADA. EMS
aggregates data, runs optimization algorithms, and issues control commands back to plant
controllers. Redundant servers and communication paths ensure availability.

**Interfaces:** SCADA/EMS connect to TSO systems (ICCP, OPC, API) for exchange of schedules,
setpoints, and status. Security (firewalls, DMZ, authentication) is implemented per
regulatory and corporate standards.

**Failure Modes:** When SCADA or EMS fails, fallback procedures define local control
modes, manual setpoints, and escalation. Regular drills validate these procedures.
"""  # noqa: E501

version = "0.0.1"
