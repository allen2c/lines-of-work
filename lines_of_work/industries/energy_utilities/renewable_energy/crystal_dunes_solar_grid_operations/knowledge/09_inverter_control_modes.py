title = "Inverter Control Modes and Setpoints"

content = """
Inverters convert DC from solar panels to AC for the grid. They can operate in several
control modes: active power control (MPPT, power limit, or dispatch setpoint), reactive
power control (Q setpoint, power factor, or voltage control), and advanced modes such
as frequency droop or virtual inertia.

**Mode Selection:** The grid code and TSO requirements dictate which modes are used.
Typical configurations for Gulf plants include active power limiting with reactive power
or power factor control for voltage support.

**Setpoint Hierarchy:** TSO instructions override default EMS setpoints; EMS overrides
local defaults. The hierarchy is enforced in the control logic to avoid conflicts.

**Limits:** Inverters have thermal and electrical limits. Operations must ensure setpoints
stay within equipment capability and do not violate warranty or design conditions.
"""  # noqa: E501

version = "0.0.1"
