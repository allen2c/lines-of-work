title = "Troubleshooting: No Light"

content = """
- Check ONT PON LED: if off, no optical signal. Use VFL at NAP end to see if red light appears at ONT connector. If yes, fiber is continuous; check ONT port.
- If VFL shows no light at ONT, go to NAP. Connect VFL to distribution fiber; if light appears at drop cable end, splice or connector issue. If not, OLT port may be dead.
- Use OTDR from NAP to trace drop cable. Look for a complete break (high loss event with no end reflection). If break is within 10 ft of NAP, re-splice. If near premises, replace drop cable.
- Check all connectors with microscope; clean if dirty. Re-terminate if endface is scratched or pitted.
- If fiber is intact but no light, measure launch power at NAP with power meter. If < +2 dBm, escalate to NOC for OLT port issue.
"""  # noqa: E501

version = "0.0.1"
