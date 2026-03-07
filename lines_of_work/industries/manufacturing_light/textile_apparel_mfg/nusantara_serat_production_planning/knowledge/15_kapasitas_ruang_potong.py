"""Cutting room capacity planning."""

title = "Kapasitas Ruang Potong"

content = """
Ruang potong adalah bottleneck umum dalam produksi garmen. Kapasitas ditentukan oleh
jumlah meja spreading, mesin potong, dan operator. Satu lay (lapisan kain) membutuhkan
waktu spreading dan cutting yang bervariasi menurut panjang marker dan jenis kain.

**Throughput per shift:** Hitung jumlah lay yang dapat diproses per shift berdasarkan
waktu rata-rata per lay dan jam kerja. Marker yang rumit atau kain yang sulit (stretch,
slippery) memperlambat proses. Jadwalkan gaya dengan marker sederhana saat kapasitas
terbatas.

**Antrian cutting:** Order yang menunggu cutting memblokir aliran ke jahit. Prioritaskan
sesuai tanggal pengiriman dan ketergantungan lini jahit.
"""  # noqa: E501

version = "0.0.1"
