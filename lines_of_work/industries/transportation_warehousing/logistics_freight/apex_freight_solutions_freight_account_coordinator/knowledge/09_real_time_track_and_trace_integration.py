title = "Real‑Time Track and Trace Integration"

content = """
- GPS ping frequency: every 5 minutes (TL) or 15 minutes (LTL) via MacroPoint API.  
- Geo‑fence alerts: entry/exit at origin, destination, and major waypoints (±10 mi).  
- ETA recalculation engine uses historical speed profiles + real‑time traffic (HERE API).  
- Deviation threshold: > 15 minutes from planned ETA or > 20 mi off‑route triggers exception ticket.  
- Visibility shared with customer via branded portal; update cadence: every 30 minutes in‑transit, immediate on exception.
"""  # noqa: E501

version = "0.0.1"
