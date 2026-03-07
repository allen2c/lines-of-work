"""Master production schedule overview."""

title = "Jadwal Induk Produksi"

content = """
Jadwal induk produksi (MPS) adalah rencana agregat yang menghubungkan permintaan
pelanggan dengan kapasitas pabrik. MPS mencakup periode mingguan atau bulanan,
menunjukkan gaya mana yang diproduksi, kapan, dan dalam jumlah berapa.

**Input MPS:** Order yang dikonfirmasi, peramalan permintaan, dan kapasitas tersedia.
MPS harus feasible—tidak melebihi kapasitas cutting, jahit, dan finishing. Revisi MPS
saat order baru masuk atau kapasitas berubah.

**Output MPS:** Rilis ke perencanaan detail (cut order, line loading) dan perencanaan
bahan. MPS adalah dokumen hidup yang diperbarui secara teratur.
"""  # noqa: E501

version = "0.0.1"
