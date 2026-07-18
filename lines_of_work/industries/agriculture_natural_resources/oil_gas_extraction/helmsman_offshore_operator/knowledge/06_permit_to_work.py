title = "Permit-to-Work (PTW) System"

content = """
- Five permit types: Cold Work (CW), Hot Work (HW), Confined Space Entry (CSE), Electrical Isolation (EI), and Lifting Operation (LO). Permits live in PermitVision with paper backup on the PTW-OP-001 series.
- Permit lifetime: maximum 12 h for HW, 8 h for CSE, 24 h for CW. Gas test certificate valid 4 h (HW) or 1 h (CSE re-entry).
- The issuer must: (1) confirm a specific task description; (2) verify the area is gas-tested to LEL <1 %, O₂ 19.5–23 %, H₂S <10 ppm, CO <25 ppm; (3) confirm isolations (valves locked, electrical LOTO, blinds installed) match the isolation register; (4) identify PPE (FR coveralls minimum, plus task-specific); (5) sign as Issuer; receiver signs as Receiver; both sign on closeout.
- Cross-references: a CSE cannot start until the CW for blinding is in place; HW requires adjacent CSE permits already closed out.
- HW must not be issued within 11 m of an open hydrocarbon source (live flange, atmospheric vent, drain) without a documented risk assessment and continuous gas monitoring.
- Any alarm or process upset auto-suspends all open HW and CSE permits; permits are re-validated, not just re-signed.
"""  # noqa: E501

version = "0.0.1"
