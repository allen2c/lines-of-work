"""Package types: QFP, BGA, CSP, and variants."""

title = "Package Types: QFP, BGA, CSP"

content = """
**QFP (Quad Flat Package):** Leads extend from all four sides; gull-wing or
J-lead. Common for medium-high pin counts. Lead pitch can be 0.5 mm, 0.4 mm
(fine-pitch), or lower. **PLCC (Plastic Leaded Chip Carrier):** J-leads; older
style but still used. **QFN (Quad Flat No-Lead):** No outward leads; pads on
bottom. Shorter electrical path, smaller footprint. **BGA (Ball Grid Array):**
Solder balls on bottom; high pin count, better electrical/thermal than leaded.
**CSP (Chip Scale Package):** Package size close to die size; minimal form factor.
**WLCSP (Wafer-Level CSP):** No separate package; redistribution and bumps
applied at wafer level, then singulated.

Selection depends on application: cost, pin count, thermal, size, and board
assembly constraints. Each package type has specific assembly flows (e.g.,
BGA uses substrate instead of leadframe; WLCSP skips wire bonding).
"""  # noqa: E501

version = "0.0.1"
