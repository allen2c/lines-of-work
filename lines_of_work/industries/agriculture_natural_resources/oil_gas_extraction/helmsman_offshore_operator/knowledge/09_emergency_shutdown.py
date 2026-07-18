title = "Emergency Shutdown (ESD) Operation"

content = """
- On confirmed fire or unignited gas release: blow the platform horn (3 long, 1 short), call "ESD-1, ESD-1, ESD-1, location and source" on Channel 1, then the OIM initiates ESD-0 if escalation is required.
- ESD-0 actions (automatic): all ESD-0 valves close; rotating equipment trips; ESDV on the CATS riser closes; well DHSVs close; firewater pumps start; deluge opens to the fire-affected zone; emergency lighting on; PA announces "Platform Shutdown, Muster at Stations".
- Operator actions after ESD-0: confirm on the ESD mimic panel that all valves in the "ESD-0" column are red; check fire pump status (P-501A/B green); account for personnel at muster stations by radio head-count; report status to OIM every 5 min.
- ESD-1 actions: all process block valves close, rotating equipment trips, depressurise to flare via BDV lines at a maximum 5 barg/min, emergency lighting on, PA announcement.
- Reset of ESD-1 / ESD-2 only after OIM authorisation, all input conditions cleared, all valves verified closed, all personnel accounted for; reset is a controlled sequence per OP-ESD-002; ESD-0 reset is by the OIM only with concurrence of the onshore Operations Manager.
- Abandonment: if the OIM orders evacuation, muster at the LQM, launch the 50-person free-fall lifeboats, call the standby helicopter and ERRV.
"""  # noqa: E501

version = "0.0.1"
