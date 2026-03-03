"""Wire sweep during molding and mitigation."""

title = "Wire Sweep"

content = """
Wire sweep is displacement of wire bonds during transfer molding when the
flowing mold compound pushes the wires. Excessive sweep can cause wire-to-wire
shorts, wire-to-leadframe shorts, or wire breakage. Sweep is measured as
maximum displacement from the original position; specs typically limit sweep
to a fraction of wire spacing.

**Mitigation:** Lower transfer pressure and fill speed reduce flow-induced
stress. Mold design (gate location, runner geometry) affects flow pattern;
simulation can optimize. Wire loop height and span influence stiffness;
lower, shorter loops are less susceptible but must meet electrical and
mechanical constraints. Compound viscosity and temperature also affect flow.
**Design:** Avoid long, high loops in high-flow regions. Process development
includes mold flow simulation and sweep measurement on representative units.
"""  # noqa: E501

version = "0.0.1"
