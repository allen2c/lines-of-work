title = "MILSTRIP Requisitions"

content = """
- MILSTRIP (Military Standard Requisitioning and Issue Procedures) is used for all supply requests. Document identifier codes (DICs) define the transaction type: A0A (stock replenishment), A04 (emergency), A06 (requisition for repair parts), etc.
- Requisitions are entered into ULLS-G and transmitted to the supporting Supply Support Activity (SSA) via the Standard Army Retail Supply System (SARSS). The SSA processes and issues materiel from the Defense Logistics Agency (DLA) or Army inventory.
- Each requisition must include: UIC (Unit Identification Code), NSN, quantity, unit of issue, required delivery date, and priority designator (01-15, with 01 highest). Emergency requisitions (A04) use priority 01-03 and require commander approval.
- Track requisition status daily using the ULLS-G “Requisition Status” report. If a requisition is backordered more than 30 days, submit a follow-up (DIC A0B). If more than 60 days, escalate to S4 for possible lateral transfer from another unit.
"""

version = "0.0.1"
