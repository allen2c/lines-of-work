title = "Proses Manajemen Perubahan"

content = """
- Setiap perubahan pada infrastruktur produksi harus melalui RFC (Request for Change) di Jira.
- Kategori perubahan:
  - Standar: reboot server non-kritis, update firmware non-inti. Dapat dilakukan tanpa CAB asalkan dalam maintenance window.
  - Normal: penambahan VM, perubahan konfigurasi firewall, upgrade OS. Perlu disetujui CAB (rapat setiap Selasa dan Kamis).
  - Darurat: perbaikan keamanan kritis, kegagalan hardware. Dapat dilakukan segera, tetapi harus diikuti RFC dalam 24 jam.
- Template RFC mencakup: deskripsi, justifikasi, risiko, rencana rollback, jadwal, dan persetujuan.
- Setelah implementasi, lakukan verifikasi dan tutup RFC. Jika gagal, jalankan rollback dan catat penyebab.
"""  # noqa: E501

version = "0.0.1"
