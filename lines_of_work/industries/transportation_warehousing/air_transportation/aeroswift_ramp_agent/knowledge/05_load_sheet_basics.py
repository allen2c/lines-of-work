title = "Load Sheet Basics"

content = """
- The load sheet is a document that shows the aircraft’s weight and balance for the flight. It includes: aircraft empty weight (EW), crew weight, fuel weight, payload (passengers + baggage + cargo), zero fuel weight (ZFW), ramp weight, takeoff weight (TOW), and landing weight.
- The ramp agent’s role is to verify that the actual loaded weights match the load sheet. Use the AeroSwift LPS to compare planned vs. actual.
- Key limits: ZFW must not exceed max ZFW (e.g., A320: 64,500 kg). TOW must not exceed max TOW (78,000 kg). Landing weight must not exceed max landing weight (66,000 kg).
- The load sheet also shows the center of gravity (CG) as a percentage of mean aerodynamic chord (MAC). Acceptable range for A320: 15% to 40% MAC. If CG is outside, reject and request re‑calculation.
"""  # noqa: E501

version = "0.0.1"
