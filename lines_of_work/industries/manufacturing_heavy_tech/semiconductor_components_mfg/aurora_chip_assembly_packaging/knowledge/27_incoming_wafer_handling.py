"""Incoming wafer handling and verification."""

title = "Incoming Wafer Handling"

content = """
Incoming wafers arrive from the foundry or probe test house. Verification
includes: wafer ID, lot number, quantity, and orientation. Check for visible
damage (chips, scratches, contamination). Verify that probe test (CP) has
been completed and that wafer maps or bin data are available if required.
Document receipt date and storage conditions.

**Storage:** Wafers are stored in sealed containers in controlled environment
(temp, humidity). Exposure to moisture or particles must be minimized. **Track
identity:** Wafer lot and slot/position are linked to the assembly lot
throughout the flow. Misidentification can cause mix-up and recall. Barcode
scanning at each handoff reduces error. **Handoff to dicing:** Confirm correct
wafer before mount and dice. Reject or quarantine any wafer with identity
ambiguity or quality concern. Escalate to logistics or quality if incoming
conditions are non-conforming.
"""  # noqa: E501

version = "0.0.1"
