"""Process control limits and SPC."""

title = "Process Control Limits"

content = """
Critical process parameters are controlled within specification limits. Control
limits (UCL/LCL) are often based on historical capability (Cpk) or customer
requirements. Parameters may include: bond force, ultrasonic power, mold
temperature, transfer pressure, plating thickness, etc. Data is collected
from equipment or manual measurement and entered into SPC charts.

**Out-of-control:** When a parameter exceeds control limits or shows a run,
trend, or shift, the process is out of control. Response: investigate cause,
contain affected product, and correct before resuming. **Capability:** Cpk
(Cp, Cpk) indicates whether the process can consistently meet spec. Cpk ≥1.33
is commonly required for critical parameters. Low capability triggers
process improvement or relaxation of spec (with customer agreement). **Review:**
Regular management review of SPC and capability drives continuous improvement.
"""  # noqa: E501

version = "0.0.1"
