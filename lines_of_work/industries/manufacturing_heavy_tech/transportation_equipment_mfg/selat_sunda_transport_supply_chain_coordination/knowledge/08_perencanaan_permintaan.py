"""Perencanaan permintaan bahan dan koordinasi dengan produksi."""

title = "Perencanaan Permintaan"

content = """
Perencanaan permintaan menghubungkan rencana produksi dengan kebutuhan bahan baku dan
komponen. Input utama: master production schedule (MPS), bill of materials (BOM), dan
data inventori saat ini. Output: kebutuhan net untuk setiap item dan tanggal
kebutuhan.

**Proses**: MRP menjalankan perhitungan kebutuhan berdasarkan MPS dan lead time.
Hasilnya adalah planned order yang dikonversi menjadi purchase order atau production
order. Perubahan jadwal produksi memerlukan rerun MRP dan penyesuaian PO.

**Koordinasi**: Berkomunikasi dengan production planning untuk setiap perubahan MPS
besar. Pastikan forecast yang diberikan ke pemasok konsisten dengan rencana internal.
"""  # noqa: E501

version = "0.0.1"
