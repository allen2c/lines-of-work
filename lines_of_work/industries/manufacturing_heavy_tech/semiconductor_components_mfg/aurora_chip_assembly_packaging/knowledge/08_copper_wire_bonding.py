"""Copper wire bonding and cost/performance trade-offs."""

title = "Copper Wire Bonding"

content = """
Copper (Cu) wire bonding has gained adoption as a lower-cost alternative to gold,
with comparable or better electrical conductivity. Cu wire requires modified
process conditions: typically a forming gas (N2/H2) atmosphere to prevent
oxidation during the free-air ball formation, and higher force/ultrasonic
parameters than Au.

**Challenges:** Cu is harder than Au; excessive force can cause pad cratering or
under-pad damage. Cu is also more susceptible to corrosion in humid environments,
so package moisture sensitivity and storage conditions must be carefully managed.
Cu bonding typically requires Au or Pd-coated pads rather than bare Al to ensure
reliable bonds and avoid Al-Cu galvanic corrosion.

**Process controls:** Forming gas flow and purity; EFO and bond parameters;
capillary design for Cu (different tip geometry than Au). Regular ball shear,
wire pull, and corrosion testing per JEDEC are essential. Recipe changes require
validation before production release.
"""  # noqa: E501

version = "0.0.1"
