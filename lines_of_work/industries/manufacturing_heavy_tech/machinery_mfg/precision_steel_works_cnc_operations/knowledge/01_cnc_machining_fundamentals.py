title = "CNC Machining Fundamentals and Coordinate Systems"

content = """
CNC (Computer Numerical Control) machining is a subtractive manufacturing process
where pre-programmed computer software dictates the movement of factory tools and
machinery. The fundamental principle involves removing material from a workpiece
using rotary cutting tools to achieve desired geometries.

**Coordinate System (Cartesian):**
All CNC machines operate on a 3D Cartesian coordinate system with X, Y, and Z axes.
The Z-axis typically aligns with the spindle (tool rotation axis), while X and Y
define the horizontal plane. Additional rotary axes (A, B, C) enable multi-axis
machining for complex contours.

**Absolute vs. Incremental Positioning:**
- **Absolute (G90):** All coordinates reference a fixed origin (machine zero or
  work zero). Every command specifies the exact position from the origin.
- **Incremental (G91):** Coordinates reference the current tool position. Each
  command specifies the distance to move from where the tool currently is.

**Work Coordinate Systems (WCS):**
Modern CNC controllers support multiple work offsets (G54 through G59.3), allowing
operators to set up several workpieces or fixtures simultaneously. Each offset stores
the distance from machine zero to the part zero location.

**Linear and Circular Interpolation:**
- **G01:** Linear interpolation moves the tool in a straight line at a specified
  feed rate (F), controlling the cutting action.
- **G02/G03:** Circular interpolation creates arcs clockwise (G02) or counter-
  clockwise (G03), requiring endpoint coordinates and either the arc center (I, J, K)
  or arc radius (R).

**Feed Rate and Spindle Speed:**
Feed rate (F) controls how fast the tool advances through material, typically in
mm/min or mm/rev. Spindle speed (S) in RPM determines the cutting surface speed.
Proper balance between feed and speed ensures chip formation, surface finish,
and tool life optimization.
"""

version = "0.0.1"
