"""Color allocation across production batches."""

title = "Alokasi Warna"

content = """
Alokasi warna mengatur urutan produksi per color dalam satu style. Memengaruhi
efisiensi dye lot, perubahan mesin, dan aliran material.

**Prinsip:** Kelompokkan warna serupa untuk minimize color changeover. Dark colors
biasanya diproduksi berurutan untuk mengurangi cleaning mesin.

**Dye lot:** Untuk fabric yang di-dye, pastikan satu batch produksi menggunakan
satu dye lot untuk konsistensi warna. Split batch jika dye lot terbatas.

**Customer requirement:** Beberapa customer meminta ship by color. Jadwalkan
sesuai prioritas pengiriman per color.
"""  # noqa: E501

version = "0.0.1"
