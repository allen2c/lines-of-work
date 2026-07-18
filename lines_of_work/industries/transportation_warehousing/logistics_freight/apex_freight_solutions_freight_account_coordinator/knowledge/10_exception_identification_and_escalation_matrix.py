title = "Exception Identification and Escalation Matrix"

content = """
- Exception categories: Late Pickup, Late Delivery, Detention, Damage/Shortage, HAZMAT Incident, Equipment Failure, Documentation Missing.  
- Auto‑creation rules: TMS monitors timestamps, POD status, driver messages; creates ticket with severity (Low/Medium/High/Critical).  
- Escalation timelines: Low – resolve within 8 h; Medium – 4 h; High – 2 h; Critical – 30 min (notify VP Ops).  
- Owner assignment: Coordinator for Low/Medium; Senior Account Manager for High; VP Ops for Critical.  
- Resolution documentation mandatory: root cause, corrective action, carrier acknowledgment, closure timestamp.
"""  # noqa: E501

version = "0.0.1"
