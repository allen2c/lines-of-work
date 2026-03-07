"""Carton allocation for packing and shipping."""

title = "Alokasi Karton untuk Packing"

content = """
Alokasi karton harus direncanakan berdasarkan ukuran karton, jumlah pieces per karton,
dan volume pengiriman. Kekurangan karton menghentikan packing dan menunda pengiriman.

**Ukuran karton:** Pilih ukuran yang meminimalkan void dan memenuhi batas berat
pengiriman. Terlalu besar meningkatkan biaya pengiriman; terlalu kecil meningkatkan
jumlah karton.

**Pieces per karton:** Sesuaikan dengan persyaratan pelanggan. Beberapa pelanggan
meminta mix size dalam satu karton; yang lain meminta single size.

**Lead time:** Pesan karton dengan lead time yang memadai. Karton custom memerlukan
waktu produksi lebih lama daripada stok standar.
"""  # noqa: E501

version = "0.0.1"
