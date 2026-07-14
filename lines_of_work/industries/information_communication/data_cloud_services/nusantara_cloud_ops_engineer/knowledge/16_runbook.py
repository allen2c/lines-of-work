title = "Runbook Operasi Rutin"

content = """
- Pemeriksaan harian (setiap shift):
  - Cek dashboard Zabbix: tidak ada alert kritis yang belum diakui.
  - Cek suhu dan kelembaban di BMS: pastikan dalam rentang normal.
  - Cek status UPS dan generator: mode normal, tidak ada alarm.
  - Cek kapasitas storage: jika >85%, catat dan rencanakan.
  - Cek log keamanan (Splunk): tidak ada anomali.
- Pemeriksaan mingguan:
  - Uji backup restore pada VM test.
  - Bersihkan log lama (lebih dari 30 hari) dari server.
  - Periksa kebersihan filter CRAC.
- Pemeriksaan bulanan:
  - Uji coba generator selama 30 menit dengan beban.
  - Audit inventaris aset (cocokkan fisik dengan database).
  - Review laporan kapasitas dan SLA.
"""  # noqa: E501

version = "0.0.1"
