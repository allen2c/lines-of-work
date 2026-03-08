"""Dasar Material Requirements Planning dalam pengadaan."""

title = "MRP Dasar"

content = """
Material Requirements Planning (MRP) adalah sistem perencanaan yang menghitung kebutuhan
bahan berdasarkan rencana produksi, BOM, dan inventori. MRP menghasilkan planned order
untuk pembelian atau produksi internal, dengan tanggal release dan due date.

**Input**: Master production schedule, BOM, on-hand inventory, scheduled receipts, dan
lead time. **Output**: Planned order release, order yang perlu dipercepat atau ditunda.

**Dalam praktik**: Jalankan MRP secara teratur (harian atau mingguan). Review exception
messages (shortage, overdue, excess) dan ambil tindakan. Konversi planned order ke PO
sesuai policy (otomatis atau manual release).
"""  # noqa: E501

version = "0.0.1"
