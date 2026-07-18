title = "Activation Process"

content = """
- After ONT syncs and Ethernet is working, call NOC or use activation portal. Provide job ID, ONT serial number, and MAC address.
- NOC will register ONT on OLT and provision services (internet, voice, IPTV). Wait for confirmation (typically 5–10 minutes).
- Verify internet: browse to a test site, run speed test (download/upload should be within 90% of plan speed). For voice, make a test call to a known number.
- For IPTV, connect set-top box to ONT’s second Ethernet port (if separate VLAN) and verify channel streaming.
- If activation fails, check ONT registration status in portal; if “unregistered,” re-verify serial number and MAC. Escalate to NOC if needed.
- Once all services confirmed, complete work order in mobile app: upload photos, test results, and customer signature.
"""  # noqa: E501

version = "0.0.1"
