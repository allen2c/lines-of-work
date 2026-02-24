title = "Overlay Control and Alignment"

content = """
Overlay refers to the precision with which one circuit layer is aligned to 
the previous layer. In modern chips with dozens of layers, overlay errors 
must be kept below 2-3 nanometers to prevent short circuits or open contacts.

**Alignment Marks:**
Wafers contain specialized "alignment marks" etched into the silicon or 
previous layers. The scanner's alignment system "reads" these marks before 
exposure to determine the exact position and orientation of the existing 
patterns on the wafer.

**Overlay Error Components:**
Overlay errors are categorized into several types:
- **Translation:** Simple X or Y shift of the entire pattern.
- **Rotation:** The pattern is slightly rotated relative to the wafer.
- **Magnification:** The pattern is slightly larger or smaller than intended.
- **Non-linear Distortions:** Complex "high-order" errors caused by wafer 
  warpage or scanner-specific aberrations.

**Advanced Process Control (APC):**
Metrology tools measure the overlay error on "send-ahead" wafers. This data 
is fed back into the scanner's APC system, which calculates corrections 
(offsets) for the next batch of wafers. This closed-loop control is essential 
for maintaining high yield.
"""

version = "0.0.1"
