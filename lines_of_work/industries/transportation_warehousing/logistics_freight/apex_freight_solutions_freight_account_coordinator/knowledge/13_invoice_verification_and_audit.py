title = "Invoice Verification and Audit"

content = """
- Three‑way match: Rate Confirmation Sheet, TMS load record (mileage, accessorials), Proof of Delivery.  
- Automated tolerance: line‑haul ±2 %, fuel surcharge ±1 %, accessorials ±5 %.  
- Exceptions routed to Audit Queue; Coordinator reviews within 2 business days.  
- Duplicate detection: invoice number + load reference + carrier ID; flagged automatically.  
- Approved invoices moved to “Ready for Payment” batch; rejected returned with coded reason (e.g., RATE_VAR, MISSING_POD).  
- Audit log retained 7 years for SOX compliance.
"""  # noqa: E501

version = "0.0.1"
