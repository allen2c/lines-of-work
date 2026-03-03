"""Wire bonding fundamentals and interconnect technology."""

title = "Wire Bonding Fundamentals"

content = """
Wire bonding creates electrical interconnections between the die pads and the
leadframe or substrate using thin metal wires (typically gold or copper). It
remains the dominant interconnect technology for a vast majority of packaged
semiconductor devices.

**Bond types:**
- **Ball bonding:** A molten ball is formed at the wire tip, then crushed onto
  the die pad (first bond) and stitched to the leadframe (second bond). Used for
  Au and Cu wire with a capillary.
- **Wedge bonding:** The wire is pressed and ultrasonically welded at both ends.
  Used for Al wire and fine-pitch applications; compatible with aluminum pads
  without special metallization.

**Critical parameters:** Bond force, ultrasonic power, time, and temperature;
capillary or wedge tool geometry; wire diameter and purity. Improper settings
cause non-sticks, cratering, excessive deformation, or wire breakage. Bond
integrity is verified by ball shear and wire pull tests per JEDEC and
customer specifications.
"""  # noqa: E501

version = "0.0.1"
