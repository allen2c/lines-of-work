title = "Phishing Email Analysis Process"

content = """
- When a phishing ticket arrives, first verify the email headers (SPF, DKIM, DMARC) using the built-in header analyzer in Proofpoint.
- Extract URLs and attachments; submit URLs to a sandbox (FireEye) and attachments to a static analysis tool (e.g., OPSWAT).
- Check the sender domain against known malicious lists (e.g., PhishTank, internal blocklist).
- If the email is malicious: (a) block the sender domain and URLs in Proofpoint, (b) add IOCs to the SIEM watchlist, (c) notify the affected user via the client portal template.
- If suspicious but not confirmed, escalate to Tier-2 for further analysis.
- If benign (e.g., marketing email), close the ticket with “Benign – user training recommended” and add to the FP list.
"""

version = "0.0.1"
