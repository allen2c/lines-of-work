title = "Penanganan Insiden Keamanan"

content = """
- Insiden keamanan meliputi: serangan DDoS, malware, akses tidak sah, kebocoran data.
- Deteksi melalui IDS/IPS (Snort/Suricata), log firewall, dan SIEM (Splunk).
- Langkah awal:
  1. Isolasi sistem terdampak (putus koneksi jaringan atau matikan VM).
  2. Catat timestamp, IP sumber, dan jenis serangan.
  3. Laporkan ke SOC (Security Operations Center) melalui channel #security-incident.
  4. Jangan hapus log atau bukti.
- Jika terindikasi pelanggaran data, segera eskalasi ke Manajer Operasi dan Tim Hukum.
- Setelah insiden selesai, lakukan post-mortem dan perbarui runbook.
"""  # noqa: E501

version = "0.0.1"
