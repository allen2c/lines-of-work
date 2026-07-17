title = "Network Configuration"

content = """
- Standard network: single VPC/VNet with 3 subnets (public, private, data). CIDR /24 minimum. No direct internet access for private subnets.
- Premium: hub-spoke topology with transit gateway. Hub contains shared services (firewall, VPN). Spokes per environment. CIDR /16 per region.
- Enterprise: full mesh with dedicated ExpressRoute/AWS Direct Connect. BGP routing. Customer must provide on-prem CIDR ranges.
- Firewall rules: default deny inbound, allow only specific ports (443, 22 from bastion, 3306 from app tier). Use NexusCloud Firewall Manager for rule updates.
- Network monitoring: flow logs enabled, sent to centralized Log Analytics/CloudWatch. Alerts for unusual traffic patterns (threshold: >1 Gbps sustained).
"""

version = "0.0.1"
