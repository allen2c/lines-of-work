title = "Canned Cycles for Drilling, Tapping, and Boring"

content = """
Canned cycles simplify programming for common hole-making operations. A single
G-code block initiates a complete machining sequence, reducing program length
and programming effort while standardizing operations.

**Common Canned Cycle Types:**
- **G81 (Standard Drilling):** Rapid to R-plane, feed to Z-depth, rapid retract.
Basic drilling for through-holes and shallow blind holes.
- **G82 (Counterboring/Spot Drilling):** Like G81 but includes a dwell at depth
for improved bottom finish and breaking chip adhesion. Used for spot faces and
counterbores requiring clean bottoms.
- **G83 (Peck Drilling - Deep Hole):** Intermittent drilling with full retract
to R-plane or chip-break position between pecks. Clears chips and reduces heat
in deep holes (typically 3x diameter or greater).
- **G73 (High-Speed Peck Drilling):** Short peck cycles with partial retract
(chip break) rather than full retract. Faster than G83 for deep holes where
chip evacuation is manageable. Best for less demanding materials.
- **G84 (Tapping):** Synchronized tapping cycle where spindle RPM and Z-axis feed
are coordinated for proper thread pitch. Supports rigid tapping (no tap holder
required on modern machines with encoder feedback).
- **G85/G86/G89 (Boring Cycles):** Various boring cycles with different retract
modes. G85 feeds in and feeds out; G86 feeds in, spindle stops, rapid out;
G89 feeds in, dwells, feeds out. Selection depends on bore surface requirements.

**Canned Cycle Parameters:**
- **X, Y:** Hole position coordinates
- **Z:** Final drilling depth (absolute or incremental based on G90/G91)
- **R:** Reference plane (rapid approach height above workpiece)
- **Q:** Peck depth increment (G73, G83)
- **P:** Dwell time at depth in milliseconds (G82, G89)
- **F:** Feed rate
- **K:** Number of repeats (for pattern drilling with incremental positioning)

**Cycle Activation and Cancellation:**
Once a canned cycle is activated (G81-G89), it remains modal. Each subsequent
X,Y position executes the same cycle at the new location. Cancel with G80
or any G-code from group 01 (G00, G01, G02, G03).

**R-Plane Considerations:**
Set R-plane high enough to clear obstructions and chips but low enough to
minimize rapid travel time. For surfaces with varying heights, calculate
appropriate R for each hole group or use incremental R values.

**Through-Drilling Clearance:**
For through-holes, program Z-depth slightly below the actual bottom surface
(0.5-1mm or 0.020-0.040") to ensure complete breakthrough and allow for
breakout burr without stopping the drill.
"""

version = "0.0.1"
