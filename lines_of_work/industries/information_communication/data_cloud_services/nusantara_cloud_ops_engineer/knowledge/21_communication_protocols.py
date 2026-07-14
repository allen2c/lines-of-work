title = "Protokol Komunikasi"

content = """
- Internal: Gunakan Slack untuk komunikasi cepat. Channel utama: #ops-general, #alerts, #incident-critical, #incident-high, #maintenance.
- Untuk insiden kritis, buat thread di #incident-critical dengan format: [INSIDEN] [KATEGORI] [PELANGGAN] – Deskripsi singkat.
- Eksternal (pelanggan): Hanya melalui tiket Jira atau email resmi (support@ncs.co.id). Jangan gunakan Slack atau telepon pribadi.
- Template email notifikasi pelanggan:
  - Subjek: [NCS] Pemberitahuan Gangguan – [ID Tiket]
  - Isi: Waktu kejadian, layanan terdampak, perkiraan durasi, langkah yang diambil.
- Saat serah terima shift, gunakan format log: Tanggal/shift, insiden aktif, perubahan yang berlangsung, item yang perlu diwaspadai, dan kontak on-call.
"""  # noqa: E501

version = "0.0.1"
