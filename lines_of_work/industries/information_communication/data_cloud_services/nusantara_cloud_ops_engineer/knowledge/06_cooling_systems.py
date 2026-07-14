title = "Sistem Pendingin"

content = """
- Menggunakan CRAC (Computer Room Air Conditioner) dan CRAH (Computer Room Air Handler) dengan konfigurasi N+1.
- Suhu ruang data dijaga antara 18-27°C (ideal 22-24°C). Kelembaban relatif 40-60%.
- Sensor suhu dan kelembaban dipasang di setiap rak (hot aisle dan cold aisle). Data dikirim ke BMS (Building Management System).
- Threshold:
  - Suhu >27°C → alert tinggi, periksa CRAC/CRAH.
  - Suhu >30°C → alert kritis, segera aktifkan pendingin cadangan.
  - Kelembaban <35% atau >65% → alert tinggi, sesuaikan humidifier/dehumidifier.
- Pemeliharaan preventif: filter diganti setiap 3 bulan, coil dibersihkan setiap 6 bulan, dan uji beban pendingin setiap tahun.
"""  # noqa: E501

version = "0.0.1"
