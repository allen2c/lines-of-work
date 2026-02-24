title = "Identity and Access Management"

content = """
Controlling who can access which systems, data, and functions is one of the most
effective and foundational controls against both external intrusion and insider threat.
Steel Sentinel Command enforces a layered identity and access management (IAM) model
rooted in the principles of least privilege and need-to-know.

**Authentication:** All access to classified systems requires multi-factor authentication
(MFA). Common Access Cards (CAC) combined with a PIN satisfy MFA for most workstation
and network access scenarios. Systems that cannot integrate with CAC-based authentication
require an approved compensating control documented in the system's security plan.

**Privileged Access:** Administrator and service accounts carry elevated risk. Privileged
users must use dedicated privileged access workstations (PAWs) for administrative tasks,
separate from workstations used for day-to-day activities such as email and browsing.
Privileged account usage is logged and reviewed weekly for anomalous activity.

**Least Privilege:** User accounts are granted only the permissions necessary to perform
assigned duties. Role-based access control (RBAC) defines permission sets by job function.
Access reviews are conducted semi-annually; permissions not exercised in 90 days are
revoked pending re-justification.

**Account Lifecycle:** Accounts are created through a documented provisioning process
that requires supervisor approval and ISSO notification. When personnel depart or change
roles, accounts are disabled within one business day. Shared or generic accounts are
prohibited except where technically necessary, and each exception requires documented
approval and enhanced logging.

**Session Management:** Workstations lock automatically after 15 minutes of inactivity.
Remote access sessions have maximum idle and connection-duration limits. All privileged
remote sessions are recorded for potential later review.
"""

version = "0.0.1"
