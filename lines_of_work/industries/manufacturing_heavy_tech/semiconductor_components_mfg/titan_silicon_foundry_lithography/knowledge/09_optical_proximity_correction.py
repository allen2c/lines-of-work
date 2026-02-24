title = "Optical Proximity Correction (OPC)"

content = """
As feature sizes shrink below the wavelength of the light source, diffraction 
causes the printed pattern to deviate from the intended design. Optical 
Proximity Correction (OPC) is a computational technique used to compensate 
for these distortions.

**Pattern Distortions:**
Common diffraction-induced errors include "line-end shortening" (where 
lines are shorter than intended) and "corner rounding" (where sharp 
corners become rounded). These errors can lead to poor electrical 
performance or circuit failure.

**OPC Features:**
OPC software modifies the photomask design by adding sub-resolution 
features:
- **Serifs:** Small squares added to corners to maintain sharpness.
- **Hammerheads:** Extensions at the ends of lines to prevent shortening.
- **SRAF (Sub-Resolution Assist Features):** Thin lines placed near 
  main features to improve their focus and dose latitude. These are 
  too small to be printed themselves.

**Model-Based OPC:**
Modern OPC uses complex mathematical models of the lithography process 
to predict how a pattern will print and then iteratively adjusts the 
mask design to achieve the desired result. This requires massive 
computational power.
"""

version = "0.0.1"
