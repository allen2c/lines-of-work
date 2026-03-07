"""Material requirements planning (MRP) process."""

title = "Perencanaan Kebutuhan Material (MRP)"

content = """
MRP menghitung kapan dan berapa banyak bahan yang harus dipesan berdasarkan jadwal
produksi dan lead time pemasok. Sistem MRP menggunakan BOM dan MPS untuk menghasilkan
purchase requisition dan planned order release. Tanpa MRP yang akurat, pabrik mengalami
kekurangan atau kelebihan bahan.

**Lead time offset:** Jika produksi dimulai minggu ke-4 dan lead time kain 3 minggu,
pemesanan harus dilakukan minggu ke-1. MRP otomatis menghitung offset ini untuk semua
komponen.

**Lot sizing:** Pemesanan dalam batch (MOQ, economic order quantity) mempengaruhi
jadwal. MRP dapat menyarankan lot sizing yang meminimalkan biaya sambil memenuhi
jadwal.
"""  # noqa: E501

version = "0.0.1"
