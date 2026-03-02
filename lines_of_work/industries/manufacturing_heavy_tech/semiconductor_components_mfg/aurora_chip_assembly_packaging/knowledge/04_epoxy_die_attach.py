"""Epoxy-based die attach process and controls."""

title = "Epoxy Die Attach"

content = """
Epoxy die attach uses conductive or non-conductive adhesives to bond the die to the
substrate. Conductive epoxies contain silver or other metal fillers for electrical
and thermal conductivity; non-conductive epoxies (NCE) provide electrical isolation
between die and substrate.

**Process steps:**
1. Dispense: Epoxy is dispensed in a pattern (dots, lines, or full coverage) onto
   the substrate or die backside.
2. Pick and place: Die is placed onto the adhesive with controlled force and dwell.
3. Cure: The assembly enters a curing oven or inline heater. Cure profiles (e.g.,
   150–175°C for 60–120 minutes) are specified by the epoxy supplier and must be
   followed to achieve full cross-linking.

**Control parameters:** Dispense volume, pattern, viscosity, and pot life; placement
force and dwell; cure temperature profile and atmosphere (N2 preferred to limit
oxidation). Void levels are measured via C-SAM ( acoustic microscopy); typical
specs allow less than 5–10% void area. Material lot traceability is mandatory.
"""  # noqa: E501

version = "0.0.1"
