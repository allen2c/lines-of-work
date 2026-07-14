title = "Sistem Tiket dan Alur Kerja"

content = """
- Gunakan Jira Service Management dengan proyek "NCS Operations".
- Jenis tiket: Insiden, Permintaan Layanan, Perubahan (RFC), Masalah (Problem).
- Alur tiket insiden:
  1. Dibuat otomatis dari alert atau manual oleh pelanggan.
  2. Assign ke insinyur yang sedang shift.
  3. Status: Baru → Diterima → Dalam Penanganan → Selesai → Ditutup.
  4. Wajib diisi: kategori, prioritas, dampak, urgensi, deskripsi, dan lampiran log.
- SLA diukur dari waktu buka hingga selesai. Jika melebihi SLA, tiket otomatis eskalasi ke manajer.
- Setiap tiket harus memiliki komentar minimal setiap 2 jam untuk insiden kritis, setiap 4 jam untuk tinggi.
- Tutup tiket hanya setelah verifikasi dengan pelanggan (jika eksternal) atau setelah pengujian internal.
"""  # noqa: E501

version = "0.0.1"
