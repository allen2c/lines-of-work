title = "Gas Compression Train K-301 / K-302"

content = """
- K-301 1st stage: centrifugal, 1.8 MW, suction 4.5 barg, discharge 18 barg, normal flow 35 000 Sm³/d; K-302 2nd stage: centrifugal, 2.4 MW, suction 17.5 barg, discharge 65 barg, normal flow 38 000 Sm³/d.
- K-301 is driven by gas turbine GT-301 (Solar Mars 100, 3.0 MW ISO); K-302 is driven by electric motor M-302 (3.3 kV, VSD).
- Anti-surge: recycle valves PV-301A around K-301 and PV-302A around K-302; the anti-surge controller opens the recycle on flow drop within 3 s. Alarm AAH-3012 at 4 % below the surge line.
- ESD-2 for compression: trip driver, close suction and discharge valves, blow down to flare; verify closure time <3 s.
- Operator checks: lube oil PI-3014 >1.8 barg, bearing temp <85 °C (trip 95 °C), vibration PI-3018 <6 mm/s RMS (trip 11 mm/s), seal gas 0.5–1.0 barg above suction.
- Fuel gas from V-301 scrubber outlet, regulated to 6.5 barg at FGR-301; GT-301 trips if pressure <5.0 barg for 30 s.
- Daily: drain V-301 knock-out pot (30 L per shift), sample drain liquid, log to E-Log; weekly: change fuel gas filter F-301.
"""  # noqa: E501

version = "0.0.1"
