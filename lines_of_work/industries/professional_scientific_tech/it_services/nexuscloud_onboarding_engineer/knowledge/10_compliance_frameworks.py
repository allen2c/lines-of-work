title = "Compliance Frameworks"

content = """
- NexusCloud supports SOC2 Type II, ISO 27001, and PCI-DSS Level 1. Customer must specify which framework applies.
- For SOC2: ensure logging, access controls, change management, and incident response are documented. Engineer must provide evidence (screenshots, logs).
- For PCI-DSS: additional requirements - network segmentation, encryption of cardholder data, quarterly scans. Engineer must deploy dedicated PCI landing zone (separate VPC).
- For ISO 27001: risk assessment, asset inventory, and supplier management. Engineer must tag all resources with asset ID.
- Compliance validation: use NexusCloud Compliance Scanner. Run before handover. Any non-compliance blocks handover until resolved.
"""

version = "0.0.1"
