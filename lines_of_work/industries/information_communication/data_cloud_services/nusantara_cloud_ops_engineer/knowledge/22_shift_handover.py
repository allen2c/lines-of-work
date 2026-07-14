title = "Serah Terima Shift"

content = """
- Setiap shift berakhir dengan sesi serah terima selama 15 menit.
- Insinyur yang akan diganti harus menyiapkan log di Confluence dengan format:
  - Ringkasan shift: jumlah insiden, alert kritis, perubahan yang dilakukan.
  - Daftar insiden aktif: ID tiket, status, tindakan terakhir, langkah selanjutnya.
  - Perubahan yang belum selesai: RFC yang masih berjalan, risiko.
  - Catatan khusus: perangkat yang bermasalah, jadwal maintenance mendatang.
- Insinyur yang masuk harus membaca log dan mengkonfirmasi pemahaman.
- Jika ada insiden kritis yang masih berlangsung, kedua insinyur harus berkoordinasi hingga insiden stabil sebelum serah terima selesai.
- Semua komunikasi serah terima dicatat di channel #ops-handover.
"""  # noqa: E501

version = "0.0.1"
