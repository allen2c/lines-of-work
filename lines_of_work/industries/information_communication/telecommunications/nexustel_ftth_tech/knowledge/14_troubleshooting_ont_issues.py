title = "Troubleshooting: ONT Issues"

content = """
- ONT not powering on: check power outlet (use voltmeter), try different outlet. If still no power, replace power adapter. If ONT still dead, replace ONT.
- PON LED blinking continuously (never solid): ONT not syncing with OLT. Verify fiber connection, clean connector. Check OLT registration: ONT may be unregistered or wrong serial number.
- LAN LED off: Ethernet cable faulty or device not powered. Test with known good cable and laptop. If still off, ONT Ethernet port may be defective; replace ONT.
- Internet works but voice fails: check VoIP settings in ONT (SIP credentials). If correct, test with analog phone; if no dial tone, escalate to NOC for provisioning.
- IPTV stuttering: check VLAN configuration; ensure second Ethernet port is set to IPTV VLAN. Test with direct connection to set-top box.
"""  # noqa: E501

version = "0.0.1"
