title = "Integrasi dengan Marketplace (Tokopedia, Shopee, Bukalapak)"

content = """
Banyak penjual di Indonesia menjual melalui marketplace selain website sendiri.
Integrasi dengan Tokopedia, Shopee, Bukalapak, dan lainnya memungkinkan
sinkronisasi pesanan, stok, dan pengiriman dari satu dashboard atau WMS.

**Sinkronisasi Pesanan:** Pesanan dari marketplace mengalir ke sistem
fulfillment (OMS/WMS) melalui API. Setiap marketplace memiliki format dan
webhook yang berbeda. Pastikan mapping field (produk, variasi, alamat,
ongkos kirim) akurat.

**Sinkronisasi Stok:** Stok yang dijual di marketplace harus mencerminkan
stok aktual. Update real-time atau batch—tergantung volume—mencegah
overselling. Beberapa marketplace mendukung Fulfillment by Marketplace
(FBM) di mana penjual mengirim sendiri, atau Fulfillment by Seller (FBS).

**Pembuatan Resi:** Setelah paket dikirim, nomor resi harus diunggah ke
marketplace dalam waktu yang ditentukan (SLA) agar status pesanan berubah
dan pelanggan dapat melacak. Keterlambatan upload dapat menyebabkan
penalti atau pembatalan otomatis.
"""  # noqa: E501

version = "0.0.1"
