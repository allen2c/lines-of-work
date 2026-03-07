"""Packing capacity planning."""

title = "Kapasitas Packing"

content = """
Packing meliputi folding, tagging, polybag, dan kartonisasi. Kapasitas bergantung pada
jumlah stasiun packing, kompleksitas instruksi (folding khusus, multiple tags), dan
ketersediaan material packing. Kekurangan polybag atau karton menghentikan packing.

**Throughput per stasiun:** Hitung unit per jam per stasiun berdasarkan waktu standar.
Beberapa gaya membutuhkan packing premium (box individual, tissue) yang lebih lambat.
Alokasikan stasiun sesuai volume dan prioritas pengiriman.

**Koordinasi dengan shipping:** Packing harus selesai sebelum cutoff pengiriman. Jadwalkan
buffer untuk inspeksi akhir dan dokumentasi.
"""  # noqa: E501

version = "0.0.1"
