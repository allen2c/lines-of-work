"""Perencanaan urutan pemotongan untuk efisiensi penggunaan kain."""

title = "Cut Order Planning"

content = """
Cut order planning menentukan berapa banyak lapisan kain yang dipotong per ukuran dan
warna untuk memenuhi pesanan dengan sisa minimal. Urutan potong memengaruhi
efisiensi marker dan waktu spreading.

**Alokasi Ukuran:** Sesuaikan jumlah potong per ukuran dengan rasio pesanan
pelanggan. Hindari overcut lebih dari allowance yang disetujui (biasanya 3–5%).

**Batch Warna:** Kelompokkan warna yang sama untuk mengurangi pergantian rol kain
dan cuci mesin potong. Pertimbangkan ketersediaan kain per warna.

**Integrasi dengan Marker:** Cut order harus selaras dengan marker yang tersedia.
Marker efisiensi di bawah 80% memerlukan review ulang atau marker baru.
"""  # noqa: E501

version = "0.0.1"
