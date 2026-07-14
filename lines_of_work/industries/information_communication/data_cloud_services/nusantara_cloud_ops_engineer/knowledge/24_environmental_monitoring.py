title = "Monitoring Lingkungan Data Center"

content = """
- Sensor lingkungan dipasang di setiap rak dan area ruang data:
  - Suhu (thermocouple) dan kelembaban (humidity sensor).
  - Deteksi kebocoran air (water leak sensor) di bawah lantai raised floor.
  - Deteksi asap (smoke detector) di plafon.
  - Sensor getaran (vibration sensor) untuk gempa.
- Data dikirim ke BMS (Building Management System) dan diintegrasikan dengan Zabbix.
- Threshold:
  - Suhu >30°C → alarm kritis, aktifkan pendingin darurat.
  - Kelembaban <35% atau >65% → alarm tinggi, sesuaikan humidifier/dehumidifier.
  - Kebocoran air terdeteksi → alarm kritis, segera matikan listrik di area tersebut dan panggil tim pemeliharaan.
  - Asap terdeteksi → alarm kritis, evakuasi dan hubungi pemadam kebakaran.
- Pemeriksaan sensor dilakukan setiap bulan untuk memastikan kalibrasi.
"""  # noqa: E501

version = "0.0.1"
