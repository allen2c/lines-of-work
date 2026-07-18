title = "NSN & Federal Supply Classification"

content = """
- Federal Supply Group (FSG) determines storage policy class; FSC class 4-digit drives shelf-life and inspection cadence.
- Items with National Codification Bureau (NCB) flag indicating non-standard packaging require a packaging directive (PD) lookup before movement.
- Reference files: FLIS, ACOD (Authorized Catalog of NSN Data), and the in-house ANDLA NSN authority table updated weekly.
- If the FSC belongs to Group 13 (ammunition) or 14 (guided missiles), immediately route to the Class V cell; the Supply Chain Analyst does not maintain these stock numbers.
- Tools in use: DOD FLIS Web, ACOD extract, and the in-house D043 NSN resolver API.
"""  # noqa: E501

version = "0.0.1"
