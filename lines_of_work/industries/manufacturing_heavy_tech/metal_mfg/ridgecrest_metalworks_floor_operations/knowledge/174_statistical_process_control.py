title = "Statistical Process Control (SPC) Fundamentals"

content = """
Statistical Process Control (SPC) is a method of monitoring and controlling a manufacturing process using statistical methods to ensure the process operates at its full potential and produces product within specification. At Ridgecrest Metalworks, SPC is applied to key dimensional characteristics on high-volume repetitive operations where process stability and capability are monitored continuously.

Every manufacturing process has inherent variation. SPC distinguishes between two types:
- Common cause variation (natural, random): Inherent to the process; present in every unit produced. Cannot be eliminated without changing the process itself. A process with only common cause variation is said to be in statistical control (stable).
- Special cause variation (assignable cause): Results from a specific, identifiable event — a tool wearing faster than expected, a material lot with different properties, an operator error, or a machine malfunction. Special cause variation is intermittent and can and must be identified and eliminated.

SPC works by sampling the process at defined intervals, measuring a quality characteristic, and plotting the results on a control chart. Statistical control limits (upper and lower control limits, UCL and LCL) are calculated from the inherent process variation (not from specification limits). Points falling outside the control limits, or patterns within the limits (runs, trends), signal the presence of special cause variation and trigger investigation.

Process capability indices quantify how well a centered, stable process fits within specification limits:
- Cp = (USL − LSL) / (6σ): Potential capability assuming the process is perfectly centered. Cp ≥ 1.33 is typically required.
- Cpk = min[(USL − X̄)/3σ, (X̄ − LSL)/3σ]: Actual capability accounting for process centering. Cpk ≥ 1.33 is the typical minimum; Cpk ≥ 1.67 is required for critical characteristics at many customers.

Initial process capability studies are conducted during process qualification (minimum 25–30 samples from a stable process). Ongoing capability is monitored using control charts; if capability falls below the minimum Cpk, corrective action is required.

SPC at Ridgecrest uses the MES (Manufacturing Execution System) for data collection at key CNC and press operations. Operators enter measurements at defined intervals; the system calculates control limits, plots control charts, and alerts supervisors when out-of-control signals are detected.
"""

version = "0.0.1"
