title = "Strategi Picking di Gudang"

content = """
Picking adalah proses mengambil barang dari lokasi penyimpanan untuk memenuhi
pesanan. Berbagai strategi dapat diterapkan tergantung volume, tipe produk,
dan layout gudang.

**Discrete Order Picking:** Satu pemetik menangani satu pesanan dari awal
hingga selesai. Cocok untuk pesanan kompleks atau volume rendah ketika presisi
lebih penting daripada kecepatan.

**Batch Picking:** Beberapa pesanan digabung; pemetik mengambil semua barang
yang dibutuhkan dalam satu putaran melalui gudang. Mengurangi jarak tempuh
dan meningkatkan throughput saat banyak pesanan membutuhkan item populer yang
sama.

**Zone Picking:** Gudang dibagi per zona (elektronik, fashion, FMCG). Setiap
pemetik bertanggung jawab atas zona tertentu; barang dikonsolidasi di stasiun
packing. Efektif untuk gudang besar dengan banyak kategori produk.

**Pick-to-Validate:** Setiap item discan saat diambil untuk memastikan SKU
benar dan memperbarui inventori secara otomatis.
"""  # noqa: E501

version = "0.0.1"
