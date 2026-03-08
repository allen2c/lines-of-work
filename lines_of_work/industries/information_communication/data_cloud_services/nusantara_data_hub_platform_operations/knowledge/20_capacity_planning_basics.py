"""Knowledge: Capacity planning fundamentals for platform operations."""

title: str = "Dasar Perencanaan Kapasitas untuk Operasi Platform"

content: str = """
Capacity planning memastikan infrastruktur dapat menanggung beban yang diantisipasi.
Operasi platform memonitor tren dan memberikan input untuk scaling.

**Metrik Kunci:** CPU, memory, disk, network throughput, dan jumlah koneksi. Track
trend harian, mingguan, musiman.

**Proyeksi:** Gunakan historical growth rate dan event calendar (kampanye, akhir tahun).
Buffer 20–30% untuk spike tak terduga.

**Threshold:** Alert ketika utilization mendekati 70–80% untuk komponen kritis. Review
bersama Engineering untuk scaling decision: vertical vs horizontal, auto-scaling config.
"""  # noqa: E501

version: str = "0.0.1"
