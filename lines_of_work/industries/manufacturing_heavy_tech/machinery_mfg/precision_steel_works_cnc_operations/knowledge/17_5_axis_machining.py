title = "5-Axis Machining Concepts and Applications"

content = """
5-axis machining adds two rotary axes to the standard three linear axes (X, Y, Z),
enabling simultaneous multi-directional cutting. This capability transforms complex
manufacturing challenges into efficient, accurate operations.

**Axis Configurations:**
- **Table-Table (Trunnion):** Both rotary axes move the table (A and B, or A and C).
Common on smaller machines. Good for smaller parts; limited by table swing and
interference with the spindle.
- **Head-Table:** One rotary axis in the spindle head (B), one in the table (C).
Balances part size capability with accessibility.
- **Head-Head:** Both rotary axes in the spindle head. Allows large parts (table
does not tilt) and excellent accessibility but more complex kinematics and
calibration requirements.

**Simultaneous vs. Indexed 5-Axis:**
- **Simultaneous:** All five axes move simultaneously during cutting. Enables
complex free-form surfaces, turbine blades, impellers, and ergonomic molds.
- **Indexed (3+2):** The rotary axes position the part/tool to an angle, then
lock while 3-axis cutting proceeds. Simpler programming, suitable for angled
features, multi-sided parts, and undercut access without full simultaneous motion.

**Benefits of 5-Axis Machining:**
- **Single Setup:** Machine complex parts completely in one fixture, improving
accuracy by eliminating cumulative setup errors.
- **Improved Surface Finish:** Maintain optimal tool-to-surface contact angle,
reducing scalloping and enabling better finish with larger tools.
- **Shorter Tools:** Access angled features with shorter, more rigid tools rather
than long reach tools prone to deflection and chatter.
- **Complex Geometry:** Produce parts with undercuts, compound angles, and
curved surfaces impossible in 3-axis machining.

**Programming Considerations:**
5-axis programming requires understanding of machine kinematics, tool center
point control (TCP), and collision avoidance. CAM systems generate 5-axis paths
but require proper post-processor support for the specific machine configuration.

**Tool Vector Control:**
TCP (Tool Center Point) programming commands the tool tip position and tool
orientation vector. The control calculates required axis positions based on
machine kinematics. Essential for simultaneous 5-axis work.

**Collision and Limit Checking:**
5-axis machines have complex reachable volumes and interference zones between
spindle, table, and fixtures. Simulation software checks for collisions before
machining. Machine controls also monitor for singularity points (mathematical
ambiguities in axis positions) that can cause erratic motion.

**Applications:**
Aerospace structural components, turbine blades and blisks, medical implants,
mold and die cores with deep ribs, automotive intake ports, and impellers for
pumps and compressors.
"""

version = "0.0.1"
