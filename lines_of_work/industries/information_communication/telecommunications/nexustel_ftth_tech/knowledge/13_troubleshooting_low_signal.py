title = "Troubleshooting: Low Signal"

content = """
- Received power at ONT below -24 dBm. First, clean all connectors (NAP and ONT) with alcohol wipes. Re-measure.
- If still low, use OTDR to locate high-loss events. Common causes: macrobends (bend radius < 10 mm), crushed cable, or poor splices.
- Check for tight bends at wall penetration, cable clips, or inside ONT enclosure. Straighten or re-route cable to maintain ≥ 30 mm bend radius.
- Inspect splice tray: ensure splices are not pinched or under tension. Re-splice if loss > 0.3 dB.
- If drop cable is damaged (e.g., rodent chew, water ingress), replace section using inline splice closure. Use mechanical splice only as temporary fix.
- After repairs, re-measure power; if still below -24 dBm, escalate to NOC for OLT transmit power check.
"""  # noqa: E501

version = "0.0.1"
