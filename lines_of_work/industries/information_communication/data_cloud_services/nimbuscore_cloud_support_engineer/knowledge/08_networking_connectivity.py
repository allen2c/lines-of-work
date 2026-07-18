title = "VPN, Interconnect, and Transit Gateway"

content = """
- Site-to-site VPN issues: confirm IKE version (IKEv2 is recommended), pre-shared key length (at least 32 bytes), and that the customer on-prem device's ASN does not collide with the NimbusCore-side ASN (default 64512).
- BGP session flaps are usually tied to a keepalive mismatch; default on the NimbusCore side is 30s hold / 80s keepalive.
- Direct Connect (NimbusCore Interconnect) ports come in 1G, 10G, and 100G; a single port can carry up to 50 BGP peers in the same virtual interface.
- Transit Gateway has a default packet rate of 50 Gbps per VPC attachment; the soft limit is 80% sustained, beyond which packets are dropped and a CloudWatch-equivalent metric `NCM_TGW_DropCount` spikes.
- For latency-sensitive customers, ask for `mtr` output from both sides over at least 100 packets before forming a hypothesis.
"""  # noqa: E501

version = "0.0.1"
