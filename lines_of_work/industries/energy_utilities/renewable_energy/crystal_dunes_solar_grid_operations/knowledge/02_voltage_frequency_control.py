title = "Voltage and Frequency Control at the Point of Connection"

content = """
The point of connection (POC) is the boundary between the plant and the grid. Voltage and
frequency at the POC must remain within the bands specified by the grid code to ensure
stability and power quality.

**Voltage Control:** Solar plants typically provide voltage support via reactive power
injection or absorption. Inverters are configured to maintain voltage at the POC within
the allowed range (e.g., ±5% of nominal) under normal and contingency conditions.

**Frequency Control:** Solar plants normally operate in maximum power point tracking (MPPT)
mode and do not provide primary frequency response unless specially equipped. Some modern
inverters and plants can offer synthetic inertia or frequency droop; grid codes are
evolving to require or incentivize this capability.

**Coordination:** The grid operations team coordinates with plant controllers and TSO
dispatch centers to adjust setpoints when the TSO requests voltage or frequency support.
"""  # noqa: E501

version = "0.0.1"
