title = "Supply Chain Security"

content = """
Modern cyber threats increasingly target the hardware and software supply chain as an
attack vector that bypasses traditional perimeter defenses. Compromised components
enter the environment with trusted signatures and legitimate provenance, making
detection extremely difficult after the fact.

**Software Supply Chain:** All software deployed on unit systems must be sourced from
approved repositories and verified by cryptographic hash against the vendor-published
value before installation. Open-source components integrated into internally developed
tools require a software composition analysis (SCA) scan to identify known-vulnerable
dependencies prior to use in production.

**Hardware Provenance:** Network equipment and endpoint hardware must be procured
through approved acquisition channels that include supply chain risk management (SCRM)
assessments. Components sourced from untrusted or unapproved vendors — including
gray-market resellers — are prohibited regardless of cost savings. Suspect hardware
is quarantined and reported to the supply chain risk management authority.

**Software Bill of Materials (SBOM):** Vendors providing software to the unit are
required to supply an SBOM listing all components and their versions. The SBOM is
ingested into the vulnerability management system, enabling automated alerting when
a component receives a new CVE after deployment.

**Firmware Integrity:** Network and endpoint firmware is verified against vendor-
published checksums before and after deployment. Unexpected changes to firmware
hashes on production devices are treated as a potential supply chain compromise
and trigger an immediate incident investigation.

**Third-Party Risk:** Contractors and vendors with access to unit systems are subject
to the same security requirements as internal personnel. Third-party access is
time-limited, scoped to the minimum necessary, and logged in full. Vendor remote
access sessions require a unit-controlled jump server as an intermediary.
"""

version = "0.0.1"
