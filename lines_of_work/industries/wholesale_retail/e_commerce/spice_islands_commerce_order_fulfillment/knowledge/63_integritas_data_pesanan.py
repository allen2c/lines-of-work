title = "Integritas Data dan Audit Trail Pesanan"

content = """
Setiap perubahan status pesanan, stok, atau dokumen pengiriman harus
tercatat. Audit trail mendukung investigasi, dispute resolution,
dan kepatuhan.

**Yang Dicatat:** Timestamp setiap status change, user atau sistem
yang melakukan perubahan, dan data sebelum/sesudah jika relevan.
Contoh: pesanan dialokasikan jam 10:15 oleh sistem; packing selesai
jam 11:30 oleh user X; resi diupload jam 11:35.

**Retensi:** Simpan log untuk jangka waktu yang ditentukan (mis. 1–2
tahun) sesuai kebijakan dan regulasi. Data dapat diarsipkan ke
storage yang lebih murah setelah periode aktif.

**Akses:** Batasi akses ke log untuk mencegah manipulasi. Tim support
dan compliance mungkin memerlukan akses read-only untuk investigasi
dispute atau keluhan.
"""  # noqa: E501

version = "0.0.1"
