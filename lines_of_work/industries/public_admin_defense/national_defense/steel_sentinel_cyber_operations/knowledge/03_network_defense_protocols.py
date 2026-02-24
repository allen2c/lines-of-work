title = "Network Defense Protocols"

content = """
Defending military networks requires layered controls applied consistently across
perimeter, internal, and endpoint layers. No single control is sufficient; defense-in-
depth assumes that any individual layer will eventually fail and compensates accordingly.

**Perimeter Controls:** All traffic entering or leaving the enclave must pass through
a next-generation firewall (NGFW) configured with deny-by-default rules. Ingress
filtering blocks spoofed source addresses; egress filtering prevents data exfiltration
to unauthorized destinations. A demilitarized zone (DMZ) separates internet-facing
services from internal networks.

**Intrusion Detection and Prevention:** Network-based intrusion detection systems (NIDS)
passively monitor traffic against signature and anomaly-based rules. Inline intrusion
prevention systems (IPS) can block or quarantine malicious traffic automatically.
Tuning thresholds quarterly reduces alert fatigue while maintaining detection fidelity.

**Network Segmentation:** Enclaves are divided into security zones based on data
classification and functional role. Cross-zone traffic is controlled by firewall policy
and monitored at chokepoints. Flat networks where every host can freely communicate
are prohibited. VLAN hopping attacks must be mitigated through proper switch hardening.

**DNS Security:** DNS queries from internal hosts must be routed through internally
managed resolvers with DNS Security Extensions (DNSSEC) validation enabled. DNS
sinkholes redirect queries for known malicious domains to a logging server for
investigation rather than blocking silently.

**Proxy and SSL Inspection:** Outbound web traffic transits an authenticated forward
proxy. SSL/TLS inspection decrypts, inspects, and re-encrypts HTTPS traffic to
identify malware using encrypted channels for command-and-control communication.
Inspection certificates are issued by an internally trusted CA.
"""

version = "0.0.1"
