"""Solder plating for leadframe lead finish."""

title = "Solder Plating"

content = """
Leadframes are often plated with solder (e.g., Sn or Sn-based alloys) to
provide a solderable surface for board mounting and to protect the underlying
Cu or alloy from oxidation. Plating is applied before or after trim/form,
depending on the process flow. Electroplating and immersion plating are common
methods.

**Quality parameters:** Plating thickness (typically 100–300 microinches),
uniformity, composition, and solderability. Thin plating risks poor solder
joints; thick plating can cause bridging or tombstoning. Plating baths must
be maintained (filtration, additive replenishment, contamination control);
deviations cause discoloration, porosity, or poor adhesion.

**Lead-free:** RoHS and similar regulations require lead-free plating (e.g.,
matte Sn, Sn-Cu, Sn-Bi). Process parameters differ from Sn-Pb; reflow
compatibility and whisker risk must be evaluated. Plating lot is part of
traceability; document bath ID and plating date.
"""  # noqa: E501

version = "0.0.1"
