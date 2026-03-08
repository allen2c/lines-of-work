"""Stock count dan inventori fisik."""

title = "Stock Count"

content = """
Stock count adalah penghitungan fisik inventori untuk memastikan akurasi sistem. Cycle
count: menghitung sebagian item secara bergiliran (biasanya item A lebih sering).
Full physical count: menghitung seluruh gudang, biasanya tahunan.

**Prosedur**: Freeze transaksi bila perlu, hitung fisik, bandingkan dengan sistem,
selidiki selisih, dan lakukan adjustment. Dokumentasikan root cause untuk selisih
signifikan.

**Akurasi**: Target akurasi inventori sering 95–98%. Selisih berulang pada item tertentu
dapat mengindikasikan masalah proses (picking, receiving, scrap tidak tercatat).
"""  # noqa: E501

version = "0.0.1"
