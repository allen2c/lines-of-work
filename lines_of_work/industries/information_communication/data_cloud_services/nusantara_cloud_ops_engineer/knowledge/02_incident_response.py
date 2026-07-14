title = "Prosedur Respons Insiden"

content = """
- Deteksi: Alert dari Zabbix atau Prometheus masuk ke channel Slack #alerts. Insinyur harus mengakui (ack) dalam 2 menit.
- Triase: Tentukan level insiden berdasarkan dampak dan urgensi:
  - Kritis: Layanan down total, pelanggan utama terdampak. Response time <5 menit, resolusi target <1 jam.
  - Tinggi: Gangguan parsial, performa menurun. Response time <15 menit, resolusi target <4 jam.
  - Sedang: Gangguan minor, tidak berdampak langsung ke pelanggan. Response time <30 menit, resolusi target <8 jam.
  - Rendah: Pertanyaan atau permintaan informasi. Response time <1 jam, resolusi target <24 jam.
- Resolusi: Ikuti runbook yang sesuai. Jika tidak ada, lakukan diagnosis dengan alat seperti ping, traceroute, cek log, atau remote console.
- Dokumentasi: Catat kronologi, tindakan, dan hasil di tiket Jira. Tutup tiket hanya setelah verifikasi bahwa layanan pulih.
"""  # noqa: E501

version = "0.0.1"
