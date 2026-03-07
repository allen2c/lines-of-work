"""Finishing capacity planning."""

title = "Kapasitas Finishing"

content = """
Finishing mencakup pressing, trimming benang, inspeksi kualitas, dan persiapan packing.
Kapasitas finishing sering diabaikan dalam perencanaan tetapi dapat menjadi bottleneck
jika volume melebihi kapasitas. Mesin pressing dan stasiun inspeksi memiliki throughput
terbatas.

**Aliran ke packing:** Finishing adalah gateway terakhir sebelum packing. Keterlambatan
di sini menunda pengiriman. Jadwalkan shift finishing agar selaras dengan output jahit.
Pertimbangkan overtime atau shift tambahan saat volume tinggi.

**Inspeksi kualitas:** Waktu inspeksi per unit bervariasi menurut kompleksitas gaya.
Buffer waktu untuk rework dan reject sebelum packing.
"""  # noqa: E501

version = "0.0.1"
