"""Knowledge: Cloud connectivity and network basics."""

title: str = "Dasar Konektivitas dan Jaringan Cloud"

content: str = """
Konektivitas cloud mempengaruhi keamanan, latensi, dan throughput. Operasi platform
perlu memahami dasar jaringan untuk troubleshooting.

**VPC dan Subnet:** Virtual Private Cloud mengisolasi resource. Subnet membagi alamat
IP. Network ACL dan security group mengontrol lalu lintas.

**Koneksi ke On-Prem:** VPN atau dedicated interconnect (Direct Connect, Cloud Interconnect)
untuk koneksi aman ke data center pelanggan.

**DNS dan Load Balancer:** DNS resolves nama ke IP. Load balancer mendistribusikan
traffic dan memastikan high availability.
"""  # noqa: E501

version: str = "0.0.1"
