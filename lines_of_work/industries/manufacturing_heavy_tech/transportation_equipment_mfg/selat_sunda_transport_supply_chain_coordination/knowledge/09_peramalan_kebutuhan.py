"""Peramalan kebutuhan bahan berdasarkan historikal dan rencana."""

title = "Peramalan Kebutuhan"

content = """
Peramalan kebutuhan memprediksi volume bahan yang diperlukan di masa depan. Metode
sederhana: historical usage dikalikan tingkat produksi yang direncanakan. Metode lanjut:
statistical forecasting dengan sesonalitas dan trend.

**Penggunaan**: Peramalan digunakan untuk negosiasi kapasitas dengan pemasok, perencanaan
logistik, dan pengaturan safety stock. Akurasi peramalan berdampak pada biaya inventori
dan risiko shortage.

**Update berkala**: Bandingkan forecast vs actual; ukur forecast accuracy (MAPE, bias).
Perbaiki model jika deviasi konsisten. Koordinasi dengan sales dan production untuk
informasi demand terbaru.
"""  # noqa: E501

version = "0.0.1"
