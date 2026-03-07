"""Packaging material planning."""

title = "Perencanaan Bahan Packing"

content = """
Bahan packing (kantong, karton, tissue, hanger, polybag) harus tersedia saat
produksi selesai dan siap dikirim. Kekurangan bahan packing menunda pengiriman.

**Perhitungan kebutuhan:** Berdasarkan jumlah pieces dan spesifikasi packing
per order, perencana menghitung kebutuhan karton, kantong, dan material lain.
Wastage 2–5% ditambahkan untuk buffer.

**Lead time:** Bahan packing standar biasanya tersedia cepat; karton custom
atau packaging khusus memerlukan lead time lebih panjang. Perencana memesan
sesuai jadwal produksi dan pengiriman.

**Koordinasi dengan finishing:** Jadwal finishing dan packing menentukan
kapan bahan packing dibutuhkan. Overstock bahan packing memakan ruang dan
modal kerja.
"""  # noqa: E501

version = "0.0.1"
