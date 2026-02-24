title = "Cyber Threat Intelligence Sharing"

content = """
Sharing cyber threat intelligence (CTI) with partner organizations multiplies the
defensive value of every indicator and analytic product the unit produces. Effective
sharing requires defined processes for classification, authorization, and format
to ensure information reaches recipients in a usable and legally authorized form.

**Sharing Platforms and Channels:** Structured threat information is exchanged using
the STIX/TAXII framework, which supports machine-readable indicators that partner
SIEM platforms can ingest automatically. Human-readable products (threat advisories,
situational awareness reports) are distributed over classified email at the appropriate
classification level.

**Traffic Light Protocol (TLP):** All CTI products are labeled with a TLP designation
that governs redistribution. TLP:RED restricts information to the original recipients
only. TLP:AMBER allows sharing within the recipient's organization and with trusted
partners. TLP:GREEN permits broad community sharing. TLP:CLEAR carries no restriction.

**Partner Organizations:** Primary sharing partners include CISA's Automated Indicator
Sharing (AIS) feed for unclassified indicators, the NSA Cybersecurity Directorate for
classified national-security-relevant threat information, and coalition partner CERTs
through approved bilateral sharing arrangements. Sharing with commercial entities
requires legal review and leadership approval.

**Minimization:** Before sharing, verify that indicator reports do not inadvertently
reveal sources, methods, or collection capabilities. Sanitize products to remove
internal system names, topology details, and operational context that could benefit
an adversary if the information were to be further distributed without authorization.

**Receiving Intelligence:** Incoming indicators from partner feeds are validated before
ingestion into production detection systems. Bulk ingestion of unvalidated IOCs creates
false-positive noise. A defined process scores and prioritizes incoming feeds based on
the partner's assessed reliability and the indicator's historical detection value.
"""

version = "0.0.1"
