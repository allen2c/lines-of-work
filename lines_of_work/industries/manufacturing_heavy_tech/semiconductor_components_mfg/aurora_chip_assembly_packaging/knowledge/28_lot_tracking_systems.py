"""Lot tracking systems and MES integration."""

title = "Lot Tracking Systems"

content = """
Manufacturing Execution Systems (MES) or equivalent software track assembly
lots through the factory. At each process step, the operator or equipment
records: step completion, equipment ID, recipe ID, timestamps, and material
consumption. Lot status (released, in-process, on-hold, completed) is
maintained in real time. Alerts notify when lots exceed expected cycle time
or when hold conditions exist.

**Integration:** MES may integrate with ERP (production planning), SPC
(statistical process control), and traceability databases. Automated data
capture from equipment reduces manual entry errors. **Reporting:** Dashboards
show WIP (work in progress), throughput, yield, and defect rates. Data enables
root cause analysis and continuous improvement. **Audit trail:** All
transactions are logged. Changes to lot status or genealogy require
authorization and audit trail. System access is role-based.
"""  # noqa: E501

version = "0.0.1"
