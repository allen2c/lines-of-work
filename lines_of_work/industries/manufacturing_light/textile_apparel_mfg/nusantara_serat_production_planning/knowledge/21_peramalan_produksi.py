"""Production forecasting methods for planning."""

title = "Peramalan Produksi"

content = """
Peramalan produksi memperkirakan volume output yang dibutuhkan berdasarkan data historis,
trend musiman, dan pesanan yang sudah dikonfirmasi. Di Nusantara Serat, peramalan
digunakan untuk perencanaan kapasitas jangka menengah dan pengadaan bahan baku.

**Metode kuantitatif:** Moving average, exponential smoothing, dan analisis regresi
untuk pola permintaan yang stabil. Data penjualan 12–24 bulan terakhir menjadi dasar.

**Faktor kualitatif:** Informasi dari tim penjualan tentang kampanye promosi, peluncuran
produk baru, atau perubahan preferensi pasar. Masukkan ke model sebagai penyesuaian.

**Akurasi:** Lacak MAPE (Mean Absolute Percentage Error) per kategori produk. Target
MAPE di bawah 15% untuk item fast-moving.
"""  # noqa: E501

version = "0.0.1"
