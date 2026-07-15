title = "SCADA Alarm Management"

content = """
- SCADA system monitors: flow, pressure, turbidity, chlorine residual, pH, temperature, chemical feed rates, pump status.
- Alarm priorities: Critical (red) – immediate action; High (yellow) – respond within 15 minutes; Low (blue) – acknowledge within 1 hour.
- Critical alarms: chlorine residual < 0.2 mg/L, finished water turbidity > 1.0 NTU, pump failure, low pressure < 20 psi.
- Acknowledge all alarms within 5 minutes; log alarm type, time, and action taken.
- If a critical alarm persists > 30 minutes without resolution, escalate to shift supervisor.
"""

version = "0.0.1"
