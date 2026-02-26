title = "Alokasi Inventori dan Penetapan Stok"

content = """
Alokasi inventori menetapkan stok fisik mana yang akan memenuhi pesanan tertentu.
Keputusan ini memengaruhi kecepatan pemenuhan, biaya pengiriman, dan efisiensi
gudang.

**Multi-Gudang:** Jika Spice Islands Commerce memiliki beberapa lokasi gudang,
pilih gudang terdekat dengan tujuan pengiriman untuk mengurangi ongkos kirim dan
waktu transit. Sistem WMS biasanya menghitung prioritas berdasarkan jarak dan
ketersediaan stok.

**FIFO untuk Barang Kadaluwarsa:** Produk dengan tanggal kedaluwarsa—makanan,
kosmetik, suplemen—harus dialokasikan berdasarkan First-In, First-Out. Stok yang
lebih lama harus diprioritaskan agar tidak tertimbun di gudang.

**Hold Stock:** Setelah pesanan divalidasi dan dibayar, stok dialokasikan dan
ditahan untuk pesanan tersebut. Alokasi yang tertunda terlalu lama dapat
menyebabkan overselling jika stok habis oleh pesanan lain.
"""  # noqa: E501

version = "0.0.1"
