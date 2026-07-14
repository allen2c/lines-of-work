title = "Definisi SLA Layanan"

content = """
- SLA untuk layanan cloud NCS:
  - Uptime bulanan: 99,9% (downtime maksimal 43 menit per bulan).
  - Response time insiden kritis: <15 menit.
  - Resolution time insiden kritis: <4 jam.
  - Resolution time insiden tinggi: <8 jam.
- Untuk data center colocation:
  - Uptime daya dan pendingin: 99,99% (downtime maksimal 4,3 menit per bulan).
  - Response time untuk gangguan daya: <5 menit.
- Pelanggaran SLA dihitung per bulan. Jika uptime di bawah target, pelanggan berhak atas kredit layanan (1% dari biaya bulanan per 0,1% di bawah SLA).
- Semua downtime harus dicatat dengan bukti timestamp dari monitoring.
"""  # noqa: E501

version = "0.0.1"
