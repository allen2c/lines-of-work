title = "Scanning Barcode dan Akurasi Fulfillment"

content = """
Barcode (UPC, EAN, atau kode internal) mengidentifikasi setiap SKU secara
unik. Scanning di setiap langkah fulfillment memastikan produk benar dan
memperbarui inventori secara otomatis.

**Picking:** Pemetik memindai barcode lokasi (bin) dan barcode produk saat
mengambil barang. Jika salah SKU, sistem memberi peringatan. Ini mencegah
kesalahan shipping barang yang salah.

**Packing:** Sebelum menutup kotak, packer memindai setiap item untuk
konfirmasi. Sistem memvalidasi bahwa isi paket sesuai pesanan.

**Shipping:** Label pengiriman yang dicetak dapat berisi barcode untuk
tracking. Kurir memindai saat pickup dan saat delivery.

**Manfaat:** Mengurangi human error, memberikan audit trail, dan
menjaga akurasi inventori real-time.
"""  # noqa: E501

version = "0.0.1"
