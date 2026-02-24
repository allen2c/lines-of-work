title: str = "Cloud Networking: VPCs, Subnets, and Connectivity"

content: str = """
Cloud networking provides the isolation and connectivity required for secure 
and performant applications. The Virtual Private Cloud (VPC) is the 
foundational building block of a private network in the cloud.

**Core Components:**
1. **VPC / VNet:** A logically isolated section of the cloud where you can 
   launch resources in a virtual network that you define.
2. **Subnets:** A range of IP addresses in your VPC. Public subnets have a 
   route to the internet (via an Internet Gateway), while private subnets 
   do not.
3. **Security Groups and NACLs:** Virtual firewalls that control inbound 
   and outbound traffic. Security Groups are stateful and operate at the 
   instance level; NACLs are stateless and operate at the subnet level.

**Hybrid Connectivity:**
*   **VPN (Virtual Private Network):** An encrypted tunnel over the public 
    internet connecting an on-premises network to the VPC. Cost-effective 
    but subject to internet latency.
*   **Direct Connect / ExpressRoute:** A dedicated physical connection 
    bypassing the public internet. Provides consistent performance and 
    higher bandwidth but at a higher cost.

**VPC Peering and Transit Gateways:** Used to connect multiple VPCs 
together. Transit Gateways act as a hub, simplifying the management of 
complex "spoke" network topologies.
"""

version: str = "0.0.1"
