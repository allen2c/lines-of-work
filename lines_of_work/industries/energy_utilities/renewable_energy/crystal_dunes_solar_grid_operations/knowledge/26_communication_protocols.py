title = "Communication Protocols for TSO and Plant Interface"

content = """
Reliable communication between the plant and the TSO is essential for dispatch,
compliance, and incident response. Standard protocols (ICCP, IEC 60870-5-104, OPC,
REST API) are used depending on the TSO's systems and agreements.

**Redundancy:** Primary and backup communication paths (e.g., fiber, microwave, cellular)
reduce the risk of loss of link. Failover is tested regularly.

**Security:** Communication links are secured (encryption, authentication, firewalls)
per regulatory and corporate requirements. Unauthorized access could allow malicious
control or data theft.

**Failure Handling:** When communication is lost, fallback procedures define local
operating modes (e.g., last setpoint, MPPT, or safe curtailment) and notification
escalation. The TSO is informed of communication failures as required.
"""  # noqa: E501

version = "0.0.1"
