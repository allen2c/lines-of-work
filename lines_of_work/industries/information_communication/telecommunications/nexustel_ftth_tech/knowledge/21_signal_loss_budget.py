title = "Signal Loss Budget"

content = """
- GPON typical budget: OLT transmit +5 dBm, ONT sensitivity -28 dBm, margin 3 dB → max allowable loss 26 dB.
- For XGS-PON: OLT transmit +4 dBm, ONT sensitivity -28 dBm, margin 2 dB → max loss 26 dB.
- Components: each connector pair (mated) adds 0.3–0.5 dB loss; each fusion splice adds 0.1–0.3 dB; cable attenuation 0.4 dB/km at 1310 nm, 0.25 dB/km at 1550 nm.
- Example budget for 1 km drop: cable loss 0.25 dB (1550 nm) + 2 connectors (0.5 dB each) + 2 splices (0.2 dB each) = 1.65 dB total. Well within budget.
- If total loss exceeds 26 dB, identify and reduce high-loss events. If still over, escalate to engineering for OLT power adjustment or redesign.
- Always measure end-to-end loss with power meter; compare to budget. Document any exceedance.
"""  # noqa: E501

version = "0.0.1"
