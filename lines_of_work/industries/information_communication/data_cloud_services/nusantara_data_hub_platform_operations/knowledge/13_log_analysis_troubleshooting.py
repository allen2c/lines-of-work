"""Knowledge: Log analysis and troubleshooting techniques."""

title: str = "Analisis Log dan Teknik Troubleshooting"

content: str = """
Analisis log adalah keterampilan inti untuk diagnosis insiden. Pendekatan sistematis
mempercepat root cause identification.

**Mulai dari Waktu:** Filter log berdasarkan window waktu insiden. Gunakan timestamp
dari alert atau laporan pelanggan. Perhatikan timezone.

**Pola Pencarian:** Cari error, exception, timeout, connection refused. Gunakan
full-text search atau structured query (JSON fields). Korelasi dengan trace_id.

**Konteks:** Gabungkan log dari berbagai komponen (API, worker, database). Urutan
event penting untuk memahami cascade failure.

**Alat:** Centralized log platform (ELK, Loki, CloudWatch) dengan retention yang
cukup. Simpan query berguna sebagai saved search.
"""  # noqa: E501

version: str = "0.0.1"
