"""Traceability and lot genealogy for assembly operations."""

title = "Traceability and Lot Genealogy"

content = """
Full traceability links every finished package to its constituent materials and
process history. Genealogy includes: wafer lot, die revision, epoxy/adhesive
lot, wire spool lot, leadframe lot, mold compound lot, plating lot, and
process parameters (recipe IDs, equipment, timestamps). This enables recall,
failure analysis, and root cause investigation.

**Data capture:** MES (Manufacturing Execution System) or similar software
records lot associations at each step. Barcode or RFID scanning at handoff
points ensures accuracy. Human entry is error-prone; automate where possible.
**Retention:** Genealogy data is retained per customer and regulatory
requirements (often 10+ years). Backup and auditability are critical.

**Audits:** Customers and quality systems audit traceability. Gaps or
ambiguities can result in lot hold or rejection. Never release a lot with
incomplete or inconsistent genealogy; stop and resolve before shipment.
"""  # noqa: E501

version = "0.0.1"
