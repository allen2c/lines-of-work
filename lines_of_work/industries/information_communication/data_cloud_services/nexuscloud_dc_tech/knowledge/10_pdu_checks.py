title = "PDU (Power Distribution Unit) Checks"

content = """
- Perform daily visual inspection of all rack PDUs: check for LED status (green = normal, red = fault), physical damage, and loose connections.
- Record voltage (target 208V ± 5% for single‑phase, 480V ± 5% for three‑phase) and current per phase.
- Calculate load percentage: (measured current / rated current) × 100. Flag if > 80%.
- Check PDU display for any alarms (overload, phase imbalance, high temperature). Log readings in the shift report.
- If a PDU is in alarm, do not add any new load. Escalate to facilities for investigation.
"""

version = "0.0.1"
