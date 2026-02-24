title = "Zero Trust Architecture"

content = """
Zero trust (ZT) is a security model that assumes no user, device, or network segment
is inherently trustworthy regardless of physical or logical location. Trust is granted
dynamically based on continuous verification of identity, device health, and behavioral
signals — never on the basis of network location alone.

**Core Principles:** Zero trust rests on three foundational ideas: verify explicitly
(authenticate and authorize every request using all available data points); use least
privilege (limit access to the minimum needed for the task at hand); and assume breach
(design detection and response as if an adversary is already present in the environment).

**Identity as the Control Plane:** In a zero-trust model, identity becomes the primary
security perimeter. Strong authentication (MFA with phishing-resistant factors such as
hardware keys or smart cards) is required for every access request. Continuous access
evaluation re-checks authorization during a session, not only at login.

**Device Health Enforcement:** Access decisions incorporate device compliance signals.
A fully patched, STIG-compliant, endpoint-managed device receives broader access than
a personal or unmanaged device. Non-compliant devices are quarantined to a restricted
network segment with limited access until remediated.

**Micro-Segmentation:** Networks are subdivided into small segments with individual
access controls rather than relying on a single perimeter firewall. Lateral movement
is constrained because compromise of one segment does not grant automatic access to
adjacent segments. Software-defined networking (SDN) facilitates dynamic policy
enforcement across micro-segments.

**Transition Considerations:** Migrating from perimeter-based security to zero trust
is a multi-year program. Existing systems that cannot support modern authentication
or device health telemetry require compensating controls during the transition period.
The unit's zero-trust roadmap is reviewed annually and updated to reflect progress
and changes in the DoD Zero Trust Reference Architecture.
"""

version = "0.0.1"
