title = "Perencanaan Kapasitas"

content = """
- Monitoring kapasitas dilakukan setiap minggu dengan metrik: CPU, RAM, storage, dan bandwidth.
- Threshold untuk perencanaan:
  - CPU usage rata-rata >70% selama seminggu → pertimbangkan penambahan VM atau upgrade.
  - Storage usage >85% → rencanakan penambahan kapasitas dalam 30 hari.
  - Bandwidth >75% pada jam sibuk → tambah link atau optimasi.
- Laporan kapasitas disusun setiap bulan dan diserahkan ke Manajer Operasi.
- Untuk cloud, gunakan fitur auto-scaling jika beban fluktuatif. Tetapkan min/max instance.
- Proyeksi pertumbuhan: berdasarkan data historis 6 bulan, hitung tren linear. Jika proyeksi melebihi kapasitas dalam 3 bulan, ajukan RFC untuk penambahan sumber daya.
"""  # noqa: E501

version = "0.0.1"
