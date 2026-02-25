title = "G-Code Programming Essentials"

content = """
G-code is the programming language used to control CNC machines. It consists of
text commands that direct machine movements, spindle operations, coolant flow,
and other auxiliary functions.

**Program Structure:**
A well-formed G-code program begins with a program number (O####), followed by
safety blocks (G21 for metric, G90 for absolute positioning, G17 for XY plane
selection), then the machining operations, and concludes with program end (M30)
or return (M99 for subprograms).

**Preparatory G-Codes (G##):**
- **G00:** Rapid positioning (non-cutting move at maximum speed)
- **G01:** Linear interpolation (cutting feed)
- **G02/G03:** Circular interpolation (clockwise/counter-clockwise)
- **G17/G18/G19:** Plane selection (XY/ZX/YZ)
- **G20/G21:** Unit selection (inch/metric)
- **G28:** Return to machine reference position
- **G40/G41/G42:** Cutter compensation (cancel/left/right)
- **G43:** Tool length compensation
- **G54-G59.3:** Work coordinate system selection
- **G81-G89:** Canned cycles (drilling, tapping, boring)

**Miscellaneous M-Codes (M##):**
- **M00:** Program stop (operator intervention required)
- **M01:** Optional stop (respects optional stop switch)
- **M03/M04/M05:** Spindle control (clockwise/counter-clockwise/stop)
- **M06:** Automatic tool change (ATC)
- **M08/M09:** Coolant control (on/off)
- **M30:** Program end and reset
- **M98/M99:** Subprogram call and return

**Address Words:**
- **X, Y, Z, A, B, C:** Axis coordinates
- **F:** Feed rate
- **S:** Spindle speed
- **T:** Tool number
- **D:** Cutter compensation register
- **H:** Tool length compensation register
- **R:** Reference plane (in canned cycles) or arc radius
- **I, J, K:** Arc center coordinates

**Modal vs. Non-Modal Commands:**
Modal commands remain active until replaced (G01, M03), while non-modal commands
execute once and do not persist (G04 dwell, G28 home return). Understanding
modality prevents unexpected machine behavior between program blocks.
"""

version = "0.0.1"
