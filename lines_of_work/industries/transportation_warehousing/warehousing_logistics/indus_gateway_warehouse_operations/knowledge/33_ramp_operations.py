"""Ramp and dock operations for Indus Gateway."""

title = "Ramp and Dock Operations"

content = """
The receiving and shipping ramp is the interface between warehouse and transport.
Efficient ramp operations minimize truck dwell time and avoid congestion.

**Receiving:** Trucks check in at gate. Dock assignment based on load type and
equipment. Unloading sequence: verify seal, open doors, count/weigh, inspect,
then move to putaway or cross-dock. Document any discrepancies before driver leaves.

**Shipping:** Orders staged at dock by carrier and route. Load sequence follows
delivery route where applicable. Seal applied, B/L or manifest signed, gate-out
recorded. Driver receives copy of shipping documents.

**Scheduling:** Appointment slots for high-volume customers reduce peak congestion.
Walk-ins accommodated when capacity allows. Peak seasons may require extended
ramp hours.
"""  # noqa: E501

version = "0.0.1"
