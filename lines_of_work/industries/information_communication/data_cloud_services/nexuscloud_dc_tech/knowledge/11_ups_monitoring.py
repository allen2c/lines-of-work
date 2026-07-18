title = "UPS (Uninterruptible Power Supply) Monitoring"

content = """
- UPS status is displayed on the BMS and local UPS panel. Check daily: battery voltage, load %, runtime remaining, and alarms.
- Normal battery voltage per cell: 2.0V – 2.25V (for lead‑acid). If any cell is below 1.9V, flag for maintenance.
- Load should not exceed 80% of UPS rating. If runtime remaining drops below 10 minutes, notify facilities.
- If UPS is in bypass mode, log the reason and expected return to normal. Bypass mode reduces protection.
- After any power event, verify UPS returns to normal mode and batteries are recharging.
"""

version = "0.0.1"
