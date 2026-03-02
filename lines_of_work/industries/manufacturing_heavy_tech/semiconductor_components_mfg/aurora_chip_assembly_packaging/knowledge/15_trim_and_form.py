"""Trim and form operations for leadframe packages."""

title = "Trim and Form"

content = """
Trim and form transforms the molded leadframe strip into individual packages
with leads shaped for mounting (e.g., gull-wing for QFP, J-lead for PLCC).
The process uses progressive dies or single-station tooling to trim excess
material and form the lead profiles.

**Trim:** Removes the dam bar and tie bars connecting the leads, separating
the leadframe outline from the strip. Trim quality affects lead coplanarity
and mechanical integrity. **Form:** Bends the leads to the specified geometry.
Form height, span, and toe-in/toe-out are critical for board-level assembly;
deviations cause placement or soldering defects.

**Quality checks:** Lead coplanarity (e.g., within 0.1 mm for fine-pitch),
lead integrity (no cracks or bends), and dimensions per drawing. Tool wear
affects consistency; preventive maintenance and replacement schedules must
be followed. Dross or burrs from trimming can cause shorts; inspect and
clean as needed.
"""  # noqa: E501

version = "0.0.1"
