title = "Process Safety and ESD Hierarchy"

content = """
- ESD levels: ESD-0 (platform total, fired by OIM pushbutton, fire, or loss of firewater >50 %); ESD-1 (process, fired by deck fire, large gas detection, or OIM); ESD-2 (unit, fired by HH level in V-201, HH pressure, or loss of driver on a compressor); PSD (process shutdown, instrument-level, automatic only).
- The ESD Cause & Effect document CE-ESD-001 (Rev 7) maps every input to every output valve; the controlled copy lives in the CCR and must not be deviated from.
- SIL ratings per IEC 61511: ESD-0 and ESD-1 valves at SIL 2, PSD loops at SIL 1. Proof test interval: 12 months for ESD-0/1 valves, 6 months for PSD.
- The BPCS (DCS) is not a safety layer; safety functions are physical valves, transmitters, and logic solvers; an IPL must never be bypassed without an Override Permit signed by OIM and HSE.
- Bow-tie reviews cover the Major Accident Hazards: well blowout, ship collision, dropped object, H₂S release; the operator shift brief includes a daily MAH review.
- Daily process safety KPIs sent onshore: trips, overrides in place, open maintenance overrides, MOC open, near-miss count.
"""  # noqa: E501

version = "0.0.1"
