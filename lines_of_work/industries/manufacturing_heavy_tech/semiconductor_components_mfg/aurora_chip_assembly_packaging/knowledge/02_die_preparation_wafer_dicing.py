"""Die preparation and wafer dicing for assembly."""

title = "Die Preparation and Wafer Dicing"

content = """
Die preparation transforms a fully tested wafer into individual dies ready for assembly.
The process begins with wafer mount: the wafer is mounted (face-up or face-down) onto a
dicing tape or film frame to prevent die shifting during dicing.

**Dicing methods:**
- **Blade dicing:** A rotating diamond blade cuts through the wafer along saw streets.
  Kerf width, spindle speed, and feed rate affect die edge quality and chipping.
- **Laser dicing:** A laser ablates or stealth-dices the wafer, useful for thin wafers
  and low-k dielectrics where blade stress causes cracking.
- **Stealth dicing:** Laser creates a modified layer inside the wafer; mechanical
  expansion separates dies with minimal debris.

**Quality checks:** Verify die integrity (no cracks, no chipping), correct orientation
(both mechanical and electrical), and tape adhesion before die pick. Reject dies with
visible defects or incorrect alignment. Die pick-and-place systems retrieve dies from
the tape and place them onto leadframes or substrates with precise positional accuracy.
"""  # noqa: E501

version = "0.0.1"
