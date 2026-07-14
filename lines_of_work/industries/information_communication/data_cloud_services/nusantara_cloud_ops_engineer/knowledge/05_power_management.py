title = "Manajemen Daya Listrik"

content = """
- Sumber daya utama: PLN dengan dua jalur terpisah (A dan B) dari gardu berbeda.
- UPS (Uninterruptible Power Supply) dengan baterai lithium-ion, runtime minimal 15 menit pada beban penuh.
- Generator diesel (2 unit, masing-masing 1 MW) otomatis menyala dalam 10 detik setelah listrik padam. Bahan bakar cukup untuk 24 jam operasi penuh.
- PDU (Power Distribution Unit) memonitor beban per rak. Beban maksimal per rak: 7 kW. Jika melebihi 80% (5,6 kW), timbul alert.
- Prosedur saat listrik padam:
  1. Verifikasi UPS aktif dan generator menyala.
  2. Pantau beban UPS dan suhu ruang.
  3. Jika generator gagal, segera hubungi vendor dan eskalasi ke manajer.
  4. Setelah listrik pulih, pastikan semua PDU dan perangkat kembali normal.
"""  # noqa: E501

version = "0.0.1"
