"""Pelacakan batch dan lot untuk traceability."""

title = "Pelacakan Batch"

content = """
Traceability mensyaratkan kemampuan melacak part dari batch/lot hingga pemasok dan
bahkan ke material source. Dalam otomotif, recall memerlukan traceability lengkap.
Setiap receipt harus dicatat dengan lot/batch number dari pemasok.

**Sistem**: ERP dan WMS harus mendukung lot tracking. Saat receiving, capture lot
number. Saat issue ke produksi, system records which lot went to which unit. FIFO
atau FEFO untuk lot dengan expiry.

**Koordinasi**: Pastikan pemasok memberikan lot number pada setiap pengiriman.
Dokumentasi
harus lengkap untuk audit dan recall.
"""  # noqa: E501

version = "0.0.1"
