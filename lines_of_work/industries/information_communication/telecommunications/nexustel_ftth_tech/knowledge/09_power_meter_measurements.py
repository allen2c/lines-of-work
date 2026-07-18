title = "Power Meter Measurements"

content = """
- Use optical power meter with SC/APC adapter set to 1550 nm (or 1310 nm as per OLT wavelength). Zero the meter before measurement.
- At NAP, connect to distribution fiber test port; measure launch power from OLT. Expected range: +2 dBm to +5 dBm. Record value.
- At customer premises, connect drop cable to power meter; measure received power. Acceptable range: -8 dBm to -24 dBm. If below -24 dBm, troubleshoot.
- Calculate total loss: launch power minus received power. Should match OTDR total loss within ±1 dB. If discrepancy >1 dB, re-check connections and cleanliness.
- For GPON, typical loss budget: OLT transmit +5 dBm, ONT sensitivity -28 dBm, margin 3 dB, so max allowable loss 26 dB. Ensure measured loss ≤ 26 dB.
"""  # noqa: E501

version = "0.0.1"
