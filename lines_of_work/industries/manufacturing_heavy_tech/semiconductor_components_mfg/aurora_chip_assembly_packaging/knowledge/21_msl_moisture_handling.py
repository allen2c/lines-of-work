"""MSL and moisture sensitivity handling."""

title = "MSL and Moisture Sensitivity Handling"

content = """
Moisture Sensitivity Level (MSL) classifies packages by their susceptibility to
moisture-induced damage (e.g., popcorning) during reflow. JEDEC J-STD-020
defines levels from 1 (least sensitive) to 6 (most sensitive). Packages must
be stored, handled, and baked according to their MSL before board mounting.

**Floor life:** After opening a dry bag, the package has a limited time (floor
life) at a given humidity condition before it must be baked again or used.
Exceeding floor life risks popcorning. **Bake:** Moisture can be driven off by
baking (e.g., 125°C, 24 hours for MSL 3). Bake conditions vary by MSL and
package thickness. Over-bake can damage some packages.

**Tracking:** Dry-pack date, bag open time, and bake history must be recorded.
Customers may require dry-pack shipment. Reflow profile (peak temp, time above
liquidus) must be within the qualified window. Document and enforce handling
procedures to avoid MSL violations.
"""  # noqa: E501

version = "0.0.1"
