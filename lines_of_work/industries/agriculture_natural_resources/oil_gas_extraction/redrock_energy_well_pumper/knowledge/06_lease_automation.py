title = "Lease Automation"

content = """
- SCADA system displays wellhead pressures, tank levels, pump status, and alarms. Check every 2 hours.
- RTU (Remote Terminal Unit) at each well: verify communication status. If offline, reboot and call SCADA support.
- Flow computer for LACT: record daily totalizer readings. Compare to manual gauge; if difference >2%, investigate.
- Alarm thresholds: high tank level (90%), low flowline pressure (20 psi), high wellhead pressure (1,100 psi). Respond within 30 minutes.
- Do not change SCADA setpoints without supervisor approval.
"""  # noqa: E501

version = "0.0.1"
