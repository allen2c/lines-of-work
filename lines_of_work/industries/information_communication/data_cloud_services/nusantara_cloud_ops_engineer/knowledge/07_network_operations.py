title = "Operasi Jaringan"

content = """
- Infrastruktur jaringan terdiri dari switch core (Cisco Nexus 9000), switch akses (Cisco Catalyst 9300), router edge (Juniper MX), dan firewall (Fortinet FortiGate).
- Protokol routing: BGP untuk koneksi ke ISP, OSPF untuk internal.
- VLAN digunakan untuk segregasi: VLAN 10 (manajemen), VLAN 20 (produksi), VLAN 30 (storage), VLAN 40 (DMZ).
- Monitoring: bandwidth usage per link, error counters, latency, packet loss. Threshold:
  - Bandwidth >80% selama 10 menit → alert tinggi.
  - Packet loss >1% → alert tinggi.
  - Link down → alert kritis.
- Prosedur saat link down: cek kabel, SFP, port status. Jika fisik OK, cek konfigurasi. Eskalasi ke L2 jika tidak pulih dalam 15 menit.
"""  # noqa: E501

version = "0.0.1"
