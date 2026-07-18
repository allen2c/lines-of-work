title = "Load Matching Algorithm Parameters"

content = """
- Primary match criteria (weight 0.4): carrier historical OTP on lane ≥ 95 %.  
- Secondary (0.25): equipment availability (dry van, reefer, flatbed) within 50 mi radius.  
- Tertiary (0.2): cost efficiency – carrier’s contracted CPM ≤ market median + 3 %.  
- Quaternary (0.15): carrier preference score (relationship, payment history).  
- Algorithm runs every 15 minutes; updates carrier rank list in real time.  
- Manual override allowed for dedicated fleet commitments; logged with reason code.
"""  # noqa: E501

version = "0.0.1"
