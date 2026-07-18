title = "Pemantauan Curah Hujan"

content = """
- Stasiun hujan otomatis (tipping bucket) dipasang di 3 titik pit. Data dikirim ke server setiap 10 menit.
- Ambang batas:
  - 0-30 mm/hari: operasi normal.
  - 30-50 mm/hari: tingkatkan kewaspadaan, periksa drainase.
  - 50-80 mm/hari: kurangi aktivitas di area rendah, aktifkan pompa tambahan.
  - > 80 mm/hari: hentikan operasi, evakuasi.
- Jika petir terlihat dalam radius 10 km, hentikan operasi dan cari shelter.
"""  # noqa: E501

version = "0.0.1"
