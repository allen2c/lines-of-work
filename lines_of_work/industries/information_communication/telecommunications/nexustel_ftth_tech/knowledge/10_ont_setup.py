title = "ONT Setup"

content = """
- Mount ONT on wall or shelf near power outlet and Ethernet drop. Ensure ventilation; do not block vents. Use provided screws and anchors.
- Connect fiber drop cable to ONT’s SC/APC port. Do not overtighten; finger-tight only. Verify green LED for PON sync (blinking during sync, solid when locked).
- Connect ONT to power adapter; plug into surge-protected outlet. Wait 2–3 minutes for boot sequence. Check LEDs: Power (green), PON (solid green), LAN (blinking if connected).
- If ONT has battery backup, install battery and test. Ensure battery LED shows green.
- Configure ONT via web interface or technician app: set VLAN ID (e.g., 100 for internet, 200 for IPTV) if required by local OLT. Default settings usually work.
- Test Ethernet port: connect laptop, verify IP address obtained (DHCP). Run speed test to confirm bandwidth matches subscribed plan.
"""  # noqa: E501

version = "0.0.1"
