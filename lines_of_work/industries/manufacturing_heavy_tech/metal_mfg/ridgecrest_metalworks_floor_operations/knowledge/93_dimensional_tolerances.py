title = "Dimensional Tolerances and Fit Systems (ISO 286)"

content = """
Dimensional tolerances define the permissible range of variation in a specified dimension, ensuring interchangeability of parts and proper function of assemblies. At Ridgecrest Metalworks, floor operators must understand how to read tolerances on engineering drawings and use appropriate measurement tools to verify conformance.

ISO 286 (also reflected in ANSI B4.1 for US customary) establishes a standardized system of tolerances for cylindrical features (shafts and holes) based on two elements: the fundamental deviation (which positions the tolerance zone relative to the nominal dimension) and the tolerance grade (International Tolerance grade, IT grade, which sets the width of the tolerance zone).

IT grades run from IT01 (finest, for gauge blocks) through IT16 (coarse, for general structural clearances). Common machining grades: IT6–IT7 for precision turning and boring, IT5–IT6 for precision grinding, IT7–IT9 for general-purpose drilling and milling. For example, a 25 mm diameter shaft at IT6 has a tolerance width of 13 µm (0.0005 inch); at IT9 it is 52 µm (0.002 inch).

Fundamental deviations are designated by a letter: uppercase letters for holes (A through Z), lowercase for shafts (a through z). Letter H (for holes) and letter h (for shafts) place the tolerance zone with one boundary at zero deviation, giving the classic unilateral tolerance.

Fit systems describe the relationship between a shaft and a hole when assembled. Clearance fits always provide clearance (shaft smaller than hole)—used for sliding and running fits. Transition fits may result in either clearance or interference—used for location fits (snug push-on). Interference fits always result in interference (shaft larger than hole)—used for press fits and force fits. Standard fit designations like H7/k6 (transition, locating) or H7/p6 (press fit) communicate complete assembly intent.

On the shop floor, operators check shaft diameters with micrometers, bore diameters with inside micrometers or bore gauges, and critical features with CMM. Go/no-go gauges provide fast pass/fail checking for high-volume production. Temperature stabilization to 68°F (20°C) is required for precision measurement since thermal expansion can alter dimensions significantly.
"""

version = "0.0.1"
