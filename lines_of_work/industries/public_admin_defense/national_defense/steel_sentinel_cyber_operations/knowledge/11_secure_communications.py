title = "Secure Communications Protocols"

content = """
Military cyber operations depend on communications channels that provide confidentiality,
integrity, and availability even under adversary interference. Every communication
carrying sensitive or operational content must use approved cryptographic protections.

**Approved Encryption Standards:** Communications are protected using NSA-approved
algorithms. For classified traffic, Type 1 encryption devices (NSA-certified hardware)
are mandatory. For sensitive-but-unclassified (SBU) traffic, FIPS 140-2/3 validated
cryptographic modules implementing AES-256 and approved key exchange protocols are
required. Commercial off-the-shelf encryption tools that lack FIPS validation are not
authorized for SBU or higher.

**Key Management:** Cryptographic keys are managed through the Electronic Key Management
System (EKMS) or its successor. Key material is treated as classified and stored in
approved containers. Keys are rotated on a defined schedule; compromise of a key
requires immediate rekeying of all affected systems. Personnel handling key material
must hold the appropriate clearance and need-to-know.

**Voice Communications:** Classified voice discussions occur over Secure Telephone
Equipment (STE) or approved VoIP systems operating on classified networks. Unclassified
cell phones and commercial VoIP platforms are not used for sensitive operational topics
regardless of environmental necessity.

**Email:** Classified email transits SIPRNet using S/MIME digital signatures and
encryption. Recipients must hold the appropriate clearance. Forwarding classified email
to a lower-classification system is strictly prohibited and constitutes a spillage event.

**Out-of-Band Channels:** Maintain a documented out-of-band (OOB) communications plan
for use when primary channels are compromised or unavailable. OOB channels are tested
quarterly as part of continuity-of-operations exercises.
"""

version = "0.0.1"
