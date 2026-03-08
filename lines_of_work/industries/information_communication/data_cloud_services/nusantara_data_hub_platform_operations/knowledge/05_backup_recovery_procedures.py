"""Knowledge: Backup and recovery operational procedures."""

title: str = "Prosedur Backup dan Recovery"

content: str = """
Backup dan recovery menjamin pemulihan data setelah kegagalan atau kehilangan.

**Jadwal Backup:** Harian untuk data transaksional; incremental atau differential
bergantung pada RPO (Recovery Point Objective). Simpan snapshot di lokasi berbeda.

**Validasi:** Restore test berkala (misalnya bulanan) untuk memastikan backup dapat
digunakan. Dokumentasikan langkah restore per layanan.

**RTO dan RPO:** RTO (Recovery Time Objective) adalah waktu maksimal pemulihan;
RPO adalah jumlah data yang dapat hilang. Keduanya mempengaruhi strategi backup.

**Escalation:** Restore produksi memerlukan persetujuan sesuai kebijakan. Laporkan
setiap kegagalan backup ke tim Security dan Engineering.
"""  # noqa: E501

version: str = "0.0.1"
