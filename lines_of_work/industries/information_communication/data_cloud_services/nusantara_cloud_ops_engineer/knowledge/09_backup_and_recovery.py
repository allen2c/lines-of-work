title = "Prosedur Backup dan Pemulihan Data"

content = """
- Backup dilakukan setiap hari (full backup mingguan, incremental harian) untuk semua VM dan database kritis.
- Retensi: backup harian disimpan 7 hari, mingguan 4 minggu, bulanan 12 bulan.
- Lokasi backup: penyimpanan lokal (NAS) dan offsite (cloud storage di region berbeda).
- Verifikasi backup: setiap hari Senin, lakukan restore test pada VM non-produksi. Catat hasil di log.
- Prosedur pemulihan:
  - Untuk VM: restore dari snapshot terakhir, pastikan integritas data.
  - Untuk database: restore dari backup SQL, lalu replay log transaksi.
  - Target RTO (Recovery Time Objective): 2 jam untuk VM kritis, 4 jam untuk non-kritis.
  - Target RPO (Recovery Point Objective): maksimal 1 jam (backup setiap jam untuk data kritis).
"""  # noqa: E501

version = "0.0.1"
