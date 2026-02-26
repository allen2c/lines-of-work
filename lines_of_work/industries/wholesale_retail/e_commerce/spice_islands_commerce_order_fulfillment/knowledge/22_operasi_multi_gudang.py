title = "Operasi Multi-Gudang"

content = """
Perusahaan dengan beberapa gudang harus mengoordinasikan stok dan
fulfillment antar lokasi. Multi-gudang mengurangi waktu pengiriman dan
ongkos kirim jika lokasi strategis dekat konsumen.

**Alokasi Pesanan:** Sistem menentukan gudang mana yang memenuhi pesanan
berdasarkan ketersediaan stok, jarak ke tujuan, dan biaya. Prioritas
dapat diset: jarak terdekat, stok tertinggi, atau biaya terendah.

**Transfer Stok:** Stok dapat dipindahkan antar gudang untuk menyeimbangkan
inventori. Transfer internal dicatat dan mempengaruhi stok di kedua lokasi.
Perencanaan transfer mempertimbangkan lead time dan permintaan prakiraan.

**Visibilitas:** Dashboard dan laporan harus menyajikan stok per gudang
dan per SKU. Tim fulfillment perlu tahu dari mana pesanan dipenuhi.
"""  # noqa: E501

version = "0.0.1"
