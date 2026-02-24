title = "Lithography Defectivity and Troubleshooting"

content = """
Defects in lithography can ruin an entire wafer or even an entire batch. 
Identifying the root cause of defects is a primary task for lithography 
engineers.

**Common Defect Types:**
- **Pattern Collapse:** High-aspect-ratio features can tip over during 
  development due to surface tension. This is mitigated by using thinner 
  resists or specialized rinse chemicals.
- **Bridging:** Unintended connections between adjacent features, often 
  caused by over-exposure, focus errors, or resist contamination.
- **Scumming:** Residual resist left in the exposed areas after 
  development, often due to insufficient dose or poor developer quality.
- **Hot Spots:** Localized focus or dose errors caused by particles on 
  the back of the wafer or the scanner's chuck.

**Automated Defect Inspection:**
Wafers are scanned using high-speed optical or electron-beam inspection 
tools. These tools compare the wafer's pattern against the design data 
(die-to-database) or against an adjacent die (die-to-die) to find 
anomalies.

**Mask Contamination:**
A single particle on the photomask can be printed on every die on the 
wafer. Photomasks are protected by thin, transparent membranes called 
"pellicles" to prevent particles from landing on the mask surface.
"""

version = "0.0.1"
