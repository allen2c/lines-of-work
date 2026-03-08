"""Manajemen backorder dan order yang tertunda."""

title = "Manajemen Backorder"

content = """
Backorder adalah order yang belum terpenuhi — pemasok belum kirim atau quantity
partial. Perlu track: expected date, reason for delay, dan impact pada produksi.
Prioritize backorder yang critical untuk production.

**Proaktif**: Follow up dengan pemasok untuk update. Jika ETA mundur, expedite atau
cari alternatif. Communicate ke production planning agar dapat adjust sequence.
Document pattern — pemasok dengan backorder kronis perlu review.

**System**: ERP harus flag backorder dan allow partial receipt. Aging report untuk
backorder yang overdue.
"""  # noqa: E501

version = "0.0.1"
