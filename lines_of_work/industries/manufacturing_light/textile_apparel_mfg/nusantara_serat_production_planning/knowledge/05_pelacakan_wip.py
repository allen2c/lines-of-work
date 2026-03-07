"""Pelacakan work-in-progress di sepanjang lini produksi."""

title = "Pelacakan Work-in-Progress"

content = """
WIP adalah barang setengah jadi yang berada di antara pemotongan dan pengiriman.
Pelacakan WIP memastikan tidak ada bottleneck tersembunyi dan aliran produksi lancar.

**Titik Pencatatan:** Pencatatan di setiap stasiun transfer: setelah potong,
setelah jahit, setelah QC in-process, setelah finishing, sebelum packing.

**Target WIP:** Batasi WIP per stasiun sesuai kapasitas. WIP berlebihan menandakan
bottleneck atau penjadwalan yang tidak seimbang.

**Sistem:** Gunakan kartu produksi, barcode, atau sistem real-time. Data WIP
digunakan untuk memperbarui jadwal dan mendeteksi keterlambatan dini.
"""  # noqa: E501

version = "0.0.1"
