"""Raw material requirements planning."""

title = "Perencanaan Kebutuhan Bahan Baku"

content = """
Setiap order produksi membutuhkan kain, benang, dan bahan pendukung dalam jumlah dan
waktu yang tepat. Kekurangan bahan menghentikan produksi; kelebihan mengunci modal
dan ruang penyimpanan. Perencanaan kebutuhan bahan (MRP) menghubungkan jadwal produksi
dengan ketersediaan bahan.

**Bill of materials:** Setiap gaya memiliki BOM yang mendefinisikan konsumsi per unit.
Konsumsi kain dihitung dari marker; trim dan aksesori dari tech pack. Lead time pemasok
menentukan kapan pemesanan harus dilakukan.

**Safety stock:** Pertahankan buffer untuk variasi konsumsi dan keterlambatan pengiriman.
Buffer yang terlalu besar meningkatkan biaya; terlalu kecil mengakibatkan line stop.
"""  # noqa: E501

version = "0.0.1"
