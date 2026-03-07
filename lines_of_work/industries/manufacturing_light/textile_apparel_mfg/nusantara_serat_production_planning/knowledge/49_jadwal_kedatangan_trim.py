"""Trim arrival scheduling."""

title = "Jadwal Kedatangan Trim"

content = """
Trim (resleting, kancing, label, benang, dll.) harus tersedia sebelum produksi
dimulai. Keterlambatan trim menghentikan lini produksi.

**Lead time trim:** Trim impor atau custom memiliki lead time panjang.
Perencana memesan trim berdasarkan MPS dengan buffer untuk keterlambatan.

**Synchronization:** Trim dan kain harus tiba dalam urutan yang memungkinkan
produksi berjalan. Trim yang tiba terlalu awal memakan ruang gudang; terlalu
lambat menunda cutting atau sewing.

**Backup plan:** Untuk trim kritis, perencana mengidentifikasi sumber alternatif
atau buffer safety stock untuk mitigasi risiko keterlambatan.
"""  # noqa: E501

version = "0.0.1"
