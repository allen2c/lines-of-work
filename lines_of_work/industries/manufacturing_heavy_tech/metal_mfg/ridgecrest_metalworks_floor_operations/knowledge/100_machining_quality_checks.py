title = "In-Process Quality Checks in Machining"

content = """
In-process quality checks during machining operations allow defects to be detected and corrected before they propagate to downstream operations or result in complete part rejection. At Ridgecrest Metalworks, the inspection plan for each part specifies what features to check, when to check them, and what measurement tools to use.

First-piece inspection is the most critical quality gate. The first part produced after any setup—new job, new shift, tool change, material lot change, or machine restart—must be fully inspected against the drawing before the remainder of the lot proceeds. First-piece inspection is performed by the operator and confirmed by Quality. Any dimension found outside tolerance requires setup adjustment and a new first piece before continuing.

In-process sampling defines how frequently subsequent pieces are inspected after the first piece is accepted. Frequency depends on process capability history, part criticality, and volume. A typical plan might specify checking critical dimensions every 10th piece and all dimensions every 25th piece. When a measurement approaches a control limit, frequency is increased.

Measurement tools and their applications: outside micrometers (shaft diameters, wall thicknesses) to ±0.0001 inch; inside micrometers and bore gauges (hole diameters) to ±0.0002 inch; depth micrometers (depths, shoulder positions); dial indicators (runout, flatness, part seating in fixture); height gauges (step heights, surface plate measurement); thread plug and ring gauges (accept/reject thread go/no-go); surface finish profilometer; optical comparator (profile check against an overlay template for complex 2D profiles).

Gauge calibration is required. All measuring instruments must be calibrated on a defined schedule traceable to NIST standards. Calibration status labels must be current. Using an out-of-calibration gauge invalidates all measurements taken with it.

Process adjustment from measurement: when a dimension drifts due to tool wear, operators adjust the appropriate tool offset (in CNC) in the direction to bring it back to target. The amount of offset change should be calculated from the measured deviation. Large sudden changes (more than 0.005 inch) indicate a problem—tool failure, workpiece slipping, thermal expansion—that requires investigation rather than a simple offset correction.
"""

version = "0.0.1"
