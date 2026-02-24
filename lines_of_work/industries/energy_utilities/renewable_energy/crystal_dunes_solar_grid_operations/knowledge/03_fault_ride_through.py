title = "Fault Ride-Through (FRT) Requirements"

content = """
Fault ride-through (FRT) is the ability of a generator to remain connected and support the
grid during voltage dips caused by faults (e.g., short circuits). Gulf grid codes define
specific voltage versus time profiles that plants must withstand without tripping.

**Voltage Dip Profiles:** Typically, the plant must stay connected for voltage dips down to
a specified residual voltage (e.g., 0% for a short period, or 20–30% for longer periods)
and must recover active and reactive power according to a defined ramp after fault clearance.

**Inverter Behavior:** Modern inverters are designed to meet FRT profiles. The grid operations
team ensures that inverter firmware and settings are updated when grid codes change and
that commissioning tests document compliance.

**Non-Compliance:** Failure to ride through faults can cause cascading trips and destabilize
the grid. Plants that trip during faults may face penalties and must demonstrate corrective
measures before reconnection.
"""  # noqa: E501

version = "0.0.1"
