title = "Cloud Security for Defense Environments"

content = """
Defense organizations increasingly leverage cloud environments for storage, computing,
and collaboration. Cloud adoption introduces unique security considerations that differ
materially from on-premises environments and require deliberate controls.

**Authorization Requirements:** Defense cloud environments must hold a current FedRAMP
authorization at the appropriate impact level (Low, Moderate, High) or a DoD equivalent
(IL2, IL4, IL5, IL6). Processing or storing classified information in commercial cloud
requires an impact level commensurate with the classification level and specific DoD
authorization. Unilaterally placing classified data in an unauthorized cloud constitutes
a classified spillage.

**Shared Responsibility Model:** Cloud security responsibilities are divided between
the cloud service provider (CSP) and the unit. The CSP typically secures the underlying
infrastructure; the unit is responsible for access control, data classification, network
configuration (security groups, VPCs), and application security. Understanding the
boundary is essential — assuming the CSP handles a control that is actually the unit's
responsibility creates exploitable gaps.

**Identity Federation and Access:** Cloud access is federated with the unit's authoritative
identity provider using SAML or OIDC. Service accounts and API keys are treated as
privileged credentials, rotated regularly, and never embedded in source code or scripts.
Cloud-native secrets management services are used to inject credentials at runtime.

**Logging and Visibility:** Cloud provider activity logs (access logs, API call logs,
data access logs) are exported to the unit's SIEM in near-real time. Gaps in cloud
logging equate to blind spots for detection. Logging coverage is validated as part of
the cloud environment's continuous monitoring plan.

**Data Residency and Sovereignty:** Classified and controlled unclassified information
(CUI) must reside in regions and data centers that meet applicable data residency
requirements. Cross-border data flows to non-approved regions are blocked by policy
configuration within the cloud environment.
"""

version = "0.0.1"
