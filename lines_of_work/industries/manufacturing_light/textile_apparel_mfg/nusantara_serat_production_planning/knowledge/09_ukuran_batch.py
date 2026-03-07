"""Penentuan ukuran batch produksi yang optimal."""

title = "Ukuran Batch Produksi"

content = """
Ukuran batch memengaruhi efisiensi setup, WIP, dan fleksibilitas. Batch terlalu
kecil: sering ganti gaya, setup tinggi. Batch terlalu besar: WIP menumpuk,
respon lambat.

**Pertimbangan:** Minimum batch untuk efisiensi marker dan spreading; MOQ
pelanggan; kapasitas harian per gaya; dan ketersediaan bahan.

**Praktik Nusantara Serat:** Batch minimum 500 potong per warna untuk gaya standar;
300 untuk gaya kompleks. Batch dapat dipecah jika ada prioritas mendesak.

**Economic Batch Quantity:** Untuk gaya repeat, hitung EBQ berdasarkan biaya setup
dan holding. Jarang diterapkan ketat di garmen karena variasi tinggi.
"""  # noqa: E501

version = "0.0.1"
