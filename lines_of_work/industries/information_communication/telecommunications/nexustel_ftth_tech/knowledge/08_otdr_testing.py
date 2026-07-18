title = "OTDR Testing"

content = """
- Connect OTDR to the fiber under test using launch cable (≥ 500 m) to eliminate dead zone. Set wavelength to 1550 nm for loss measurement (1310 nm for distance).
- Configure parameters: pulse width 10 ns for short spans (<1 km), 100 ns for longer; averaging time 30 seconds; refractive index 1.4682 (standard SMF).
- Analyze trace: identify events (splices, connectors, bends). Splice loss should be ≤ 0.3 dB; connector loss ≤ 0.5 dB; reflective events (Fresnel) at connectors are normal.
- Measure total end-to-end loss; compare to budget (typically 28 dB for GPON). If loss exceeds budget, locate high-loss events and repair.
- Save trace file with job ID and date; upload to company system. Include comments on any anomalies.
"""  # noqa: E501

version = "0.0.1"
