"""Shipping schedule coordination with production."""

title = "Jadwal Pengiriman"

content = """
Jadwal pengiriman harus selaras dengan selesainya produksi dan ketersediaan transportasi.
Terlambat pengiriman berdampak pada penalti dan kehilangan kepercayaan pelanggan.

**ETD dan ETA:** Tetapkan Estimated Time of Departure berdasarkan target selesai packing.
Komunikasikan Estimated Time of Arrival ke pelanggan dengan buffer untuk customs dan
transit.

**Moda transportasi:** Untuk ekspor, pilih sea freight atau air freight berdasarkan
urgensi dan biaya. Sea freight memerlukan perencanaan lebih awal karena lead time
lebih panjang.

**Dokumen pengiriman:** Pastikan commercial invoice, packing list, dan dokumen
kepabeanan siap sebelum pengiriman.
"""  # noqa: E501

version = "0.0.1"
