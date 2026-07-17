title = "Identity and Access Management (IAM)"

content = """
- Create a dedicated NexusCloud service account for management operations. Use least privilege: only necessary permissions for monitoring, backup, and patching.
- Customer admin users: create IAM roles with MFA enforced. Role hierarchy: Viewer, Operator, Admin. No root account usage.
- For Premium/Enterprise: integrate with customer's existing IdP (Azure AD, Okta) via SAML 2.0. Engineer must configure trust relationship.
- Temporary credentials: for initial setup, use a break-glass account with 7-day expiry. Rotate immediately after handover.
- Audit: all IAM changes logged in CloudTrail/Activity Logs. Monthly review of unused roles.
"""

version = "0.0.1"
