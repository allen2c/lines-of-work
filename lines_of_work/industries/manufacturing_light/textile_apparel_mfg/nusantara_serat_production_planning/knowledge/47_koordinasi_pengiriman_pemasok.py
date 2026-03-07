"""Supplier delivery coordination."""

title = "Koordinasi Pengiriman Pemasok"

content = """
Koordinasi pengiriman pemasok memastikan bahan baku dan trim tiba sesuai jadwal
produksi. Keterlambatan pengiriman mengganggu alur produksi dan menunda order.

**Jadwal pengiriman:** Perencana menyusun jadwal kebutuhan bahan berdasarkan
MPS dan lead time produksi. Purchase order dikirim dengan tanggal pengiriman
yang jelas.

**Follow-up:** Perencana memantau status pengiriman dan mengingatkan pemasok
sebelum tanggal jatuh tempo. Keterlambatan dilaporkan dan jadwal produksi
disesuaikan.

**Penerimaan:** Jadwal penerimaan di gudang dikoordinasikan dengan kapasitas
inspeksi dan ruang penyimpanan. Bahan yang tiba terlalu awal dapat memenuhi
gudang; terlalu lambat menunda produksi.
"""  # noqa: E501

version = "0.0.1"
