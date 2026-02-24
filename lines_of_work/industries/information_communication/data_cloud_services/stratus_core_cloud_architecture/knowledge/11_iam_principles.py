title: str = "Identity and Access Management (IAM) Principles"

content: str = """
Identity and Access Management (IAM) is the security discipline that enables 
the right individuals to access the right resources at the right times for 
the right reasons. In the cloud, IAM is the new network perimeter.

**Core IAM Concepts:**
1. **Least Privilege:** The principle of granting only the minimum 
   permissions necessary to perform a task. This reduces the "blast radius" 
   in the event of a credential compromise.
2. **Authentication (AuthN) vs. Authorization (AuthZ):** Authentication 
   verifies who a user is (e.g., via passwords, MFA); Authorization 
   determines what they are allowed to do (e.g., via policies, roles).
3. **Role-Based Access Control (RBAC):** Assigning permissions to roles 
   rather than individual users. Users are then assigned to roles, 
   simplifying management as the organization scales.

**Modern IAM Patterns:**
*   **Federated Identity:** Allowing users to sign in using their existing 
    corporate credentials (e.g., via SAML 2.0 or OIDC) rather than creating 
    new cloud-specific accounts.
*   **Just-In-Time (JIT) Access:** Granting elevated permissions only when 
    needed and for a limited duration, further enforcing least privilege.
*   **Multi-Factor Authentication (MFA):** Requiring two or more 
    verification factors, significantly increasing security over 
    password-only systems.

Architects must design IAM policies that are granular, regularly audited, 
and integrated with centralized identity providers to maintain a strong 
security posture.
"""

version: str = "0.0.1"
