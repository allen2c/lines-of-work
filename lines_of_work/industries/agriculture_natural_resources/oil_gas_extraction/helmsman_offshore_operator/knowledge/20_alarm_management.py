title = "Alarm Management and Rationalisation"

content = """
- The alarm philosophy is ISA 18.2 compliant; the target is 150 alarms per operator per day for the CCR (current average 240, with a rationalisation project in progress).
- Alarm priority colours: A1 red, A2 orange, A3 yellow, A4 blue (informational); deadbands are set to prevent chattering.
- Operator response times: A1 in 30 s, A2 in 2 min, A3 in 10 min, A4 log only.
- Shelving of alarms is permitted for a maximum of 8 h with OIM approval and a written justification in the Alarm Management log; shelved alarms are reviewed daily at the morning meeting.
- Suppression (hiding) of an alarm requires a Management of Change and a documented risk assessment; the operator may not choose to suppress.
- The annunciator uses 3 sequential tones (A1 at 2 Hz, A2 at 1 Hz, A3 at 0.5 Hz); the first-out A1 alarm is locked in until acknowledged.
- If more than 10 alarms appear in 10 min, the CRO announces "Alarm Flood" and the SO supports diagnosis; alarms are never blindly acknowledged.
- Alarm KPI: percentage acknowledged within target (target 95 %) and the top 10 nuisance alarms, prioritised for rationalisation.
"""  # noqa: E501

version = "0.0.1"
