title = "Control Charts: X-Bar, R-Chart, and P-Chart"

content = """
Control charts are the primary tool of Statistical Process Control. At Ridgecrest Metalworks, three types of control charts are in regular production use: the X-bar and R chart for variable data, and the p-chart for attribute data. Understanding how to read and react to these charts is a required competency for production supervisors and quality engineers.

X-bar chart (mean chart): Plots the average (X-bar) of each sample subgroup over time. The center line is the grand mean (X-double bar). Control limits are set at ±3 standard deviations of the subgroup means. The X-bar chart monitors the process mean — whether the process is producing at the correct level. Shifts in the mean (e.g., tool wear causing progressive drift, or a new material lot with a slightly different dimension) appear as trends or shifts on this chart.

R chart (range chart): Plots the range (maximum minus minimum) within each subgroup. The center line is the average range (R-bar). Control limits are derived from R-bar using constants that depend on subgroup size. The R chart monitors process dispersion — whether the process variation is consistent. An increase in range indicates increased process variation (e.g., tool chatter, inconsistent clamping, or mixed material).

The X-bar and R charts are used together: the process is in statistical control only when both charts show no out-of-control signals. Control limits on the X-bar chart are derived from R-bar; therefore, if the R chart is out of control, the X-bar limits are not valid.

Western Electric (WECO) rules identify out-of-control signals in addition to points outside control limits:
- One point beyond 3-sigma control limits
- Two of three consecutive points beyond 2-sigma warning limits (same side)
- Four of five consecutive points beyond 1-sigma limits (same side)
- Eight consecutive points on the same side of the center line (run rule)

P-chart (proportion non-conforming): Used when the quality characteristic is measured by attribute (pass/fail) rather than a variable. The p-chart plots the fraction of nonconforming items in each inspection sample. Control limits vary with sample size. Common applications: welding defect rate, coating holiday rate, thread gauge reject rate.

When a control chart signals an out-of-control condition at Ridgecrest, the operator contacts the supervisor immediately. The process is investigated for assignable cause, the cause is documented, and corrective action is taken. Parts produced since the last in-control point are quarantined pending 100 % inspection decision.
"""

version = "0.0.1"
