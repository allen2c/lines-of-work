title = "Overselling dan Pencegahan"

content = """
Overselling terjadi ketika penjual menerima pesanan untuk barang yang
sebenarnya sudah habis. Menyebabkan kegagalan pemenuhan, cancel order,
dan ketidakpuasan pelanggan. Pencegahan memerlukan akurasi stok real-time.

**Penyebab:** Latensi sinkronisasi stok antara channel (website, marketplace)
dan WMS; pesanan bersamaan yang melebihi stok; atau selisih inventori
antara sistem dan fisik.

**Solusi Teknis:** Reserve stok saat checkout atau saat keranjang
ditambahkan (dengan timeout); sinkronisasi stok real-time atau near-real-time
ke semua channel; buffer stok yang tidak dipublikasikan di channel
untuk margin error.

**Proses Manual:** Jika overselling terdeteksi (mis. saat picking stok
tidak ada), segera hubungi pelanggan—tawarkan penggantian, pengiriman
tertunda, atau refund. Jangan biarkan pelanggan menunggu tanpa kabar.
"""  # noqa: E501

version = "0.0.1"
