title = "Power Dispatch Protocols and Setpoints"

content = """
Power dispatch is the process of instructing the plant to produce a specified active power
output. In solar plants, this is implemented by setting power limits or curtailment setpoints
on the plant controller or energy management system (EMS).

**Dispatch Sources:** Dispatch instructions may come from the TSO (in markets with central
dispatch), from the plant's own scheduling and forecasting system, or from contractual
obligations. The grid operations team reconciles these sources and issues clear setpoints.

**Communication:** Dispatch is typically communicated via SCADA, ICCP, or similar protocols.
Redundant communication paths and fallback procedures (e.g., local setpoints when links fail)
must be documented and tested.

**Ramp Rates:** Dispatch changes must respect ramp rate limits specified in the grid code
and equipment capability. Sudden changes can stress inverters and affect grid stability.
"""  # noqa: E501

version = "0.0.1"
