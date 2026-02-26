title = "FIFO dan Manajemen Tanggal Kedaluwarsa"

content = """
First-In, First-Out memastikan stok terlama dikirim terlebih dahulu,
khususnya untuk produk dengan tanggal kedaluwarsa. Mencegah barang
kadaluwarsa sampai ke pelanggan dan mengurangi write-off.

**Produk dengan Expiry:** Makanan, kosmetik, suplemen, obat-obatan
memiliki tanggal kedaluwarsa. Saat receiving, catat batch dan expiry.
WMS harus mendukung picking berdasarkan FEFO (First Expired, First Out).

**Picking Priority:** Sistem memilih lokasi dengan stok tertua atau
expiry terdekat saat alokasi. Pemetik diarahkan ke lokasi tersebut.

**Monitoring:** Alert untuk stok yang mendekati kedaluwarsa (mis. 30 hari)
agar tim dapat melakukan promosi cepat atau redistribusi sebelum write-off.
"""  # noqa: E501

version = "0.0.1"
