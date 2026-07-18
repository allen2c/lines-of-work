title = "Load Tender Creation and Distribution"

content = """
- Tender template auto‑populated from order entry: origin/destination, commodity, weight, dimensions, equipment type, pickup/delivery windows, accessorials.  
- Mandatory fields: reference number, HAZMAT flag, appointment required (Y/N), temperature range (if reefer).  
- Distribution: simultaneous broadcast to top 5 qualified carriers per lane via TMS API; fallback to email if API fails.  
- Tender expiry: 2 hours for TL, 4 hours for LTL; auto‑re‑tender to next tier if no acceptance.  
- Acceptance confirmation triggers automatic load build, driver assignment, and POD workflow initiation.
"""  # noqa: E501

version = "0.0.1"
