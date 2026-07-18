title = "Fire and Gas Detection Matrix"

content = """
Fixed detectors cover all process areas. The Board Operator monitors the F&G map on the DCS for alarms. Voting logic (2oo3) is used for critical shutdown triggers to prevent spurious trips.
*   Gas Detectors: Catalytic bead sensors for 0-100% LEL range.
*   Flame Detectors: UV/IR detectors with 30-meter range coverage.
*   Heat Detectors: Rate-of-rise heat detectors in cable trays.
*   Alarm Voting: Two gas alarms required to trigger ESD Level 2.
*   Maintenance: Bump testing schedule enforced every 30 days.
"""  # noqa: E501

version = "0.0.1"
