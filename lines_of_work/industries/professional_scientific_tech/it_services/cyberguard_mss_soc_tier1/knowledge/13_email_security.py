title = "Email Security Gateway: Proofpoint"

content = """
- Proofpoint is the email security gateway; it filters inbound and outbound emails for spam, phishing, and malware.
- The “Threat Dashboard” shows blocked emails, malicious URLs, and attachment detections.
- For phishing analysis, use the “Email Analysis” tool: paste the email headers to view SPF, DKIM, DMARC results.
- To block a sender domain: go to “Policy” > “Sender Blocklist” > add domain with reason.
- To release a quarantined email (if false positive): use “Quarantine” > select email > “Release” and add note.
- Proofpoint also provides URL click-time protection; if a user clicked a malicious URL, check the “Click Logs” for details.
"""

version = "0.0.1"
