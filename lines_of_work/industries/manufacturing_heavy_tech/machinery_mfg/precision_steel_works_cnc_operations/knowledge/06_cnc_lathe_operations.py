title = "CNC Lathe Operations and Turning Techniques"

content = """
CNC lathes rotate the workpiece against stationary cutting tools, making them
ideal for cylindrical components. Understanding lathe operations is essential
for shaft, bushing, and rotational part production.

**Primary Turning Operations:**
- **OD Turning:** Reduces outside diameter using tools fed parallel to the
rotation axis. Roughing removes material; finishing achieves tolerance and finish.
- **Facing:** Cuts perpendicular to the axis to create flat end surfaces and
establish part length.
- **Grooving and Parting:** Uses narrow tools to cut grooves or separate finished
parts from bar stock. Requires rigid setup and careful chip control.
- **Boring:** Enlarges existing holes using single-point tools on the tool post,
achieving precise internal diameters and surface finishes.
- **Threading:** Cuts internal or external threads using synchronized spindle
rotation and Z-axis feed. G32 (single pass), G76 (multi-pass canned cycle), or
G92 (simple threading cycle).

**Tool Nose Radius Compensation:**
All lathe inserts have a nose radius that affects finish and geometry. Without
compensation (G41/G42), programmed points create dimensional errors on tapers
and radii. Enter the tool nose radius in the offset page and activate compensation
for precision work.

**Centerline Alignment:**
Tools must be set on the spindle centerline. High tools create positive rake and
potential dig-in; low tools create negative rake and rubbing. Use a center height
gage or test cuts to verify alignment.

**Bar Feeder Integration:**
Automatic bar feeders enable unattended production from long bar stock. Require
proper bar preparation (straightness, diameter consistency) and collet/chuck
compatibility. Bar remaining length must be sufficient for safe clamping.

**Live Tooling (Mill-Turn Centers):**
Equipped with powered rotary tools in the turret, enabling milling, drilling,
and tapping on the lathe. Transforms the lathe into a multitasking machine,
reducing setups and improving concentricity between turned and milled features.

**Tailstock and Center Support:**
Use centers (dead or live) to support long, slender workpieces and prevent
vibration/deflection. Essential for shaft work and between-centers machining
where both ends require precision.
"""

version = "0.0.1"
